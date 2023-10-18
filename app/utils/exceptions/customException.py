from abc import abstractmethod

from fastapi.responses import JSONResponse


class CustomException(Exception):

    @abstractmethod
    def handle_and_return(self):
        return JSONResponse(status_code=500, content="Error")

    def __init__(self, message=None, exception=None):
        if message is not None:
            self.message = message
        if exception is not None:
            self.exception = exception
