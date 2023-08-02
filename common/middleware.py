import json
import logging
import traceback

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from .exception import BaseError, InternalServerError

logger = logging.getLogger(__name__)


class HandleCustomExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        default_exception = InternalServerError(None)
        status_code = default_exception.get_status_code()
        error_code = default_exception.get_error_code()
        message = default_exception.get_message()
        try:
            status_code = exception.get_status_code()
            error_code = exception.get_error_code()
            message = exception.get_message()
        except Exception as e:
            logger.exception("Unrecognised exception occured:" + str(e))
        return HttpResponse(json.dumps({"error": message, "code": error_code}), status=status_code,
                            content_type="application/json")