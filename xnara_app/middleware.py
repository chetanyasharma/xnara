import datetime
import logging


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request
        logger = logging.getLogger('django.request')
        logger.info(
            f"request-loggers :Method: {request.method}, URL: {request.path}, Headers: {request.headers},UserID:{request.user.id}")

        response = self.get_response(request)
        if response.status_code == 500:
            logger = logging.getLogger('django.server_errors')
            logger.error(f'Internal Server Error on path: {request.path},api_error:{response.data}')

        # Log the response
        logger.info(f'Response status code: {response.status_code}')

        return response
