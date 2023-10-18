import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.exceptions.custom_exception import CustomException
from app.utils.exceptions.missing_authentication_exception import \
    MissingAuthenticationException
from app.utils.exceptions.unauthorized_exception import UnauthorizedException

TOKEN_PREFIX = 'Bearer '
VALID_TOKEN = "ValidToken"
SWAGGER_PATHS = ["docs", "openapi.json"]


class Middleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, next):
        try:
            self.authorize(request)
            return await next(request)
        except CustomException as e:
            # Handle controlled exceptions
            return e.handle_and_return()
        except Exception as e:
            # Handle uncontrolled exceptions
            return JSONResponse(
                status_code=500,
                content={
                    "exception": str(e),
                    "traceback": traceback.format_exc(limit=None, chain=True)
                }
            )

    def authorize(self, request: Request):
        # Check if request has to be authenticated
        if not self.needs_to_authenticate(request):
            return

        # Check token exists and it's format
        authToken = request.headers.get('Authorization')
        if authToken is None or not authToken.startswith(TOKEN_PREFIX):
            raise MissingAuthenticationException()

        # Check if token is valid (mocked)
        authToken = authToken.removeprefix(TOKEN_PREFIX)
        if authToken != VALID_TOKEN:
            raise UnauthorizedException()

    def needs_to_authenticate(self, request: Request) -> bool:
        # Assert authorization for testing
        url = request.get("url", None)
        if url is None:
            return True

        # Bypass authorization for swagger paths
        path = str(request.url).removeprefix(str(request.base_url))
        return path not in SWAGGER_PATHS or path
