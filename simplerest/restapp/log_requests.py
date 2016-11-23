import logging

logger = logging.getLogger("django.server")

def log_requests(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        logger.info("REQUEST HEADERS: \n" 
             + "\n".join([str(key) + ":" + str(value) for key, value in request.META.items()]))

        response = get_response(request)

        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Methods"] = 'POST, GET, OPTIONS'
        response["Access-Control-Allow-Headers"] = 'Authorization'

        logger.info("RESPONSE HEADERS: \n" 
             + "\n".join([str(key) + ":" + str(value) for key, value in response.items()]))

        return response

    return middleware
