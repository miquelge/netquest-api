import starlette.status as status_code
from fastapi.responses import JSONResponse

from app.utils.exceptions.custom_exception import CustomException


class NotFoundException(CustomException):
    message = "Resource not found."

    def handle_and_return(self):
        return JSONResponse(
            status_code=status_code.HTTP_404_NOT_FOUND,
            content=self.message
        )
