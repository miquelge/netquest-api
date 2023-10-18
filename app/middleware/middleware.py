import logging as log
import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from app.utils.exceptions.customException import CustomException
from app.utils.exceptions.missingAuthenticationException import \
    MissingAuthenticationException
from app.utils.exceptions.unauthorizedException import UnauthorizedException

TOKEN_PREFIX = 'Bearer '
VALID_TOKEN = "ValidToken"


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
            log.error(str(e))
            log.error(traceback.format_exc(limit=None, chain=True))
            return JSONResponse(
                status_code=500,
                content={
                    "exception": str(e),
                    "traceback": traceback.format_exc(limit=None, chain=True)
                }
            )

    def authorize(self, request: Request):
        # Check token exists and it's format
        authToken = request.headers.get('Authorization')
        if authToken is None or not authToken.startswith(TOKEN_PREFIX):
            raise MissingAuthenticationException()

        # Check if token is valid (mocked)
        authToken = authToken.removeprefix(TOKEN_PREFIX)
        if authToken != VALID_TOKEN:
            raise UnauthorizedException()
