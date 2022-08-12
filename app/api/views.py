from django.http import HttpResponse
from django.core.handlers.asgi import ASGIRequest


async def get_orders(request: ASGIRequest):
    return HttpResponse("Hello, async Django!  hf")
