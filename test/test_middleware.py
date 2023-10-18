import json

import pytest
from fastapi import Request
from starlette.responses import JSONResponse

from app.middleware.middleware import Middleware
from app.utils.exceptions.custom_exception import CustomException
from app.utils.exceptions.missing_authentication_exception import \
    MissingAuthenticationException
from app.utils.exceptions.unauthorized_exception import UnauthorizedException


class MockApp:
    async def __call__(self, request):
        return JSONResponse(content={'result': 'success'})


@pytest.fixture
def middleware():
    return Middleware(MockApp())


validRequest = Request(scope={"type": "http"})
validRequest.scope['headers'] = [
    ("authorization".encode(), "Bearer ValidToken".encode())
]


def test_middleware_authorize_valid_token(middleware):
    response = middleware.authorize(validRequest)
    assert response is None


def test_middleware_authorize_missing_token(middleware):
    request = Request(scope={"type": "http"})
    request.scope['headers'] = []
    with pytest.raises(MissingAuthenticationException):
        middleware.authorize(request)


def test_middleware_authorize_invalid_token(middleware):
    request = Request(scope={"type": "http"})
    request.scope['headers'] = [
        ("authorization".encode(), "Bearer InvalidToken".encode())
    ]
    with pytest.raises(UnauthorizedException):
        middleware.authorize(request)


@pytest.mark.asyncio
async def test_middleware_dispatch_custom_exception(middleware):
    async def mock_next(request):
        raise CustomException("Custom Error")

    response = await middleware.dispatch(validRequest, mock_next)

    assert response.status_code == 500
    assert response.body.decode('utf-8') == "Error"


@pytest.mark.asyncio
async def test_middleware_dispatch_uncontrolled_exception(middleware):
    async def mock_next(request):
        raise Exception("Uncontrolled Error")

    response = await middleware.dispatch(validRequest, mock_next)
    response_body = json.loads(response.body.decode('utf-8'))

    assert response.status_code == 500
    assert "exception" in response_body
    assert response_body["exception"] == "Uncontrolled Error"
    assert "traceback" in response_body


@pytest.mark.asyncio
async def test_middleware_dispatch_no_exception(middleware):
    async def mock_next(request):
        return JSONResponse(content={'result': 'success'})

    response = await middleware.dispatch(validRequest, mock_next)
    response_body = json.loads(response.body.decode('utf-8'))

    assert response.status_code == 200
    assert response_body == {'result': 'success'}
