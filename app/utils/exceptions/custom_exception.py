from abc import abstractmethod

import starlette.status as status_code
from fastapi.responses import PlainTextResponse


class CustomException(Exception):

    @abstractmethod
    def handle_and_return(self):
        return PlainTextResponse(
            status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
            content="Error"
        )

    def __init__(self, message=None, exception=None):
        if message is not None:
            self.message = message
        if exception is not None:
            self.exception = exception
