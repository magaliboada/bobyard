import logging
from django.http import JsonResponse, HttpRequest, HttpResponse
from backend.domain.exceptions import BaseException
from typing import Callable, Optional

logger = logging.getLogger(__name__)


class ExceptionHandlerMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            response = self.get_response(request)
            return response
        except BaseException as e:
            logger.error(f"Caught BaseException: {str(e)}", exc_info=True)
            return JsonResponse({"error": e.message}, status=e.status_code)
        except Exception as e:
            logger.error(f"Caught unexpected exception: {str(e)}", exc_info=True)
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)

    def process_exception(
        self, request: HttpRequest, exception: Exception
    ) -> Optional[HttpResponse]:
        if isinstance(exception, BaseException):
            return JsonResponse(
                {"error": exception.message}, status=exception.status_code
            )
        return None
