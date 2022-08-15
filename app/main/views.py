from django.http import HttpResponse
from django.shortcuts import render
from asgiref.sync import sync_to_async

import asyncio
from time import sleep
import httpx


# helpers
async def http_call_async():
    for num in range(1, 3):
        await asyncio.sleep(1)
        print(num)

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 3):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# views
@sync_to_async
def index(request):
    return render(request, 'main/main.html', {'title': 'Yo'})


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

def test(request):
    return render(request, 'index.html', {})
