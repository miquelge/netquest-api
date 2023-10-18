import starlette.status as status_code
from fastapi.responses import JSONResponse

from app.utils.exceptions.custom_exception import CustomException


class MissingAuthenticationException(CustomException):
    message = "The authentication header is missing or is not well formatted."

    def handle_and_return(self):
        return JSONResponse(
            status_code=status_code.HTTP_401_UNAUTHORIZED,
            content=self.message
        )
