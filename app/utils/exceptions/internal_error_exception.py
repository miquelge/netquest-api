import traceback

import starlette.status as status_code
from fastapi.responses import JSONResponse

from app.utils.exceptions.custom_exception import CustomException


class InternalErrorException(CustomException):
    message = "Internal Server Error."

    def handle_and_return(self):
        content = {
            "message": self.message,
            "traceback": traceback.format_exc(limit=None, chain=True)
        }
        if self.exception is not None:
            content["exception"] = str(self.exception)
        return JSONResponse(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
            content=content
        )
