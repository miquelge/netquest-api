from fastapi.responses import JSONResponse

from app.utils.exceptions.customException import CustomException


class MissingAuthenticationException(CustomException):
    message = "The authentication header is missing or is not well formatted."

    def handle_and_return(self):
        return JSONResponse(status_code=401, content=self.message)
