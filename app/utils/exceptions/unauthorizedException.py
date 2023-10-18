from fastapi.responses import JSONResponse

from app.utils.exceptions.customException import CustomException


class UnauthorizedException(CustomException):
    message = "Unauthorized."

    def handle_and_return(self):
        return JSONResponse(status_code=401, content=self.message)
