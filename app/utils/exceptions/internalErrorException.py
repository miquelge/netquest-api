import traceback

from fastapi.responses import JSONResponse

from app.utils.exceptions.customException import CustomException


class InternalErrorException(CustomException):
    message = "Internal Server Error."

    def handle_and_return(self):
        content = {
            "message": self.message,
            "traceback": traceback.format_exc(limit=None, chain=True)
        }
        if self.exception is not None:
            content["exception"] = str(self.exception)
        return JSONResponse(status_code=500, content=content)
