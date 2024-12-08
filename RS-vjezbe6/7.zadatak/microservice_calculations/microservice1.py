import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

async def handle_zbroj(request):
    data = await request.json()
    lista_brojeva = data.get("brojevi")
    return web.json_response({"zbroj": sum(lista_brojeva)}, status=200)

app.router.add_post("/zbroj", handle_zbroj)

web.run_app(app, port=8083)