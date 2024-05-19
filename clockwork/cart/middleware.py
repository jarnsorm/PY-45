import logging

logger = logging.getLogger('TotalLogger')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class CartLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user = request.user.username if request.user.is_authenticated else 'Pidor Anonymous'
            logger.info(f"User: '{user}': {request.method} {request.path}")
            response = self.get_response(request)
            logger.info(f"Response: {response.status_code}")
            return response
        except Exception as e:
            logger.exception(f"An error occurred: {e}")
            raise
