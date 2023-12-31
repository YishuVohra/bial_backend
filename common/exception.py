import json

from rest_framework.views import exception_handler

from .constants import ResponseConstants


def core_exception_handler(exc, context):
    # If an exception is thrown that we don't explicitly handle here, we want
    # to delegate to the default exception handler offered by DRF. If we do
    # handle this exception type, we will still want access to the response
    # generated by DRF, so we get that response up front.
    response = exception_handler(exc, context)
    handlers = {
        'ProfileDoesNotExist': _handle_generic_error,
        'ValidationError': _handle_generic_error
    }
    # This is how we identify the type of the current exception. We will use
    # this in a moment to see whether we should handle this exception or let
    # Django REST Framework do it's thing.
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        # If this exception is one that we can handle, handle it. Otherwise,
        # return the response generated earlier by the default exception 
        # handler.
        return handlers[exception_class](exc, context, response)

    return response


def _handle_generic_error(exc, context, response):
    # This is about the most straightforward exception handler we can create.
    # We take the response generated by DRF and wrap it in the `errors` key.
    response.data = {
        'errors': response.data
    }

    return response


class BaseError(Exception):
    def __init__(self, code, message, status_code):
        self.error_code = code
        if message is None:
            message = ResponseConstants.STATUS_CODES.get(code, "")
        self.message = message
        self.status_code = status_code

    def get_error_code(self):
        return self.error_code

    def get_message(self):
        try:
            return json.loads(self.message)
        except:
            return self.message

    def get_status_code(self):
        return self.status_code


class BadError(BaseError):
    def __init__(self, code: str, message = None, status_code=400):
        super().__init__(code, message, status_code)


class InternalServerError(BaseError):
    def __init__(self, message):   
        if(not message):
            message = "Something went wrong! Please try after sometime"     
        super().__init__(None, message, 500)