import logging
import uuid

logger = logging.getLogger("orienta")


class ResponsePolicy:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        correlation = uuid.uuid4().hex
        response = self.get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'none'; style-src 'self'; font-src 'self'; img-src 'self'; form-action 'self'; base-uri 'none'; frame-ancestors 'none'"
        )
        # Los formularios deben conservar un Origin verificable para CSRF.
        response["Referrer-Policy"] = "same-origin"
        response["Cache-Control"] = "no-store"
        response["X-Request-ID"] = correlation
        if response.status_code >= 400:
            # No URL, query string, alias, credential or response content in logs.
            logger.warning("http_error status=%s correlation=%s", response.status_code, correlation)
        return response
