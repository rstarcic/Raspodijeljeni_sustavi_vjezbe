import asyncio
import aiohttp
import math
from aiohttp import web

app = web.Application()

async def handle_umnozak(request):
    data = await request.json()
    lista_brojeva = data.get("brojevi")
    if not isinstance(lista_brojeva, list):
            return web.json_response({"error": "Invalid input. 'brojevi' must be a list."}, status=400)
    umnozak = 1
    for broj in lista_brojeva:
        umnozak *= broj
    return web.json_response({"umnozak": umnozak}, status=200) 
    
app.router.add_post("/umnozak", handle_umnozak)

web.run_app(app, host="localhost", port=8084)