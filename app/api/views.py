from django.http import HttpResponse, JsonResponse
from django.core.handlers.asgi import ASGIRequest
from django.views.decorators.csrf import csrf_exempt

from main.models import Peer


async def get_orders(request: ASGIRequest):
    return HttpResponse("Hello, async Django!  hf")


@csrf_exempt
def receive_data(request):
    latitude, longitude = request.POST.get('loc').split(',')
    Peer.objects.create(
        latitude = latitude,
        longitude = longitude,
        city = request.POST.get('city'),
        ip = request.POST.get('ip'),
    )
    return JsonResponse({'status': 'success'})