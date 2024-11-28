import asyncio
import aiohttp
from aiohttp import web

app = web.Application()

def handler_function(request):
    print("Hello World")
    data = {"kolegij": "Raspodijeljeni sustavi", "broj_studentata": 35}
    return web.json_response(data)

async def post_handler(request):
    data = await request.json()
    print(data)
    return web.Response(data)

app.router.add_get("/", handler_function)
app.router.add_post("/", handler_function)

web.run_app(app, host="localhost", port=8080)