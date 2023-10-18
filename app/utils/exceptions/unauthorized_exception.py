import starlette.status as status_code
from fastapi.responses import JSONResponse

from app.utils.exceptions.custom_exception import CustomException


class UnauthorizedException(CustomException):
    message = "Unauthorized."

    def handle_and_return(self):
        return JSONResponse(
            status_code=status_code.HTTP_401_UNAUTHORIZED,
            content=self.message
        )
