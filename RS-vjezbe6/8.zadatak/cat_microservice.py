import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def get_cat_facts(request):
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://catfact.ninja/facts")
        response_json = await response.json()
        return web.json_response(response_json["data"])

async def get_specific_number_of_facts(request):
    number_of_facts = int(request.match_info["amount"])
    async with aiohttp.ClientSession() as session:
        tasks = [session.get("https://catfact.ninja/fact") for _ in range(number_of_facts)]
        responses = await asyncio.gather(*tasks)
        facts = []
        for response in responses:
            print(response)
            data_json = await response.json()
            facts.append(data_json["fact"])
        return web.json_response({"facts": facts})

app.router.add_get("/cats", get_cat_facts)
app.router.add_get("/cat/{amount}", get_specific_number_of_facts)

web.run_app(app, port=8086)