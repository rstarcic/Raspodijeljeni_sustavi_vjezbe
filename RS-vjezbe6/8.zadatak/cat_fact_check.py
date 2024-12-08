import aiohttp
from aiohttp import web

app = web.Application()

async def check_if_cat_fact(request):
    data = await request.json()
    filtered_facts = [fact for fact in data["facts"] if "cat" or "cats" in fact.lower()]
    return web.json_response({ "filtered_facts": filtered_facts })
    
app.router.add_post("/facts", check_if_cat_fact)

web.run_app(app, port=8087)