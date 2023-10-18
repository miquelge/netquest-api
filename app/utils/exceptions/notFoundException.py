from fastapi.responses import JSONResponse
from app.utils.exceptions.customException import CustomException


class NotFoundException(CustomException):
    message = "Resource not found."

    def handle_and_return(self):
        return JSONResponse(status_code=404, content=self.message)

