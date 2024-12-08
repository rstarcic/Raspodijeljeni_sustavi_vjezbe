import aiohttp
import asyncio
from aiohttp import web

app = web.Application()

async def handle_service1(request):
    await asyncio.sleep(4)
    return web.json_response({"message" : "Pozdrav nakon 4 sekunde"})

app.router.add_get("/pozdrav", handle_service1)


web.run_app(app, port=8082)
