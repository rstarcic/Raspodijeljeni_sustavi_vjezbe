import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

async def handle_kolicnik(request):
    data = await request.json()
    zbroj = data.get("zbroj")
    umnozak = data.get("umnozak")
    if zbroj == 0:
        return web.json_response({"error": "Divison by zero is not possible"})
    kolicnik = umnozak / zbroj
    return web.json_response({"kolicnik": kolicnik}, status=200)

app.router.add_post("/kolicnik", handle_kolicnik)

web.run_app(app, host="localhost", port=8085)