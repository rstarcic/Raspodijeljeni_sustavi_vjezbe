"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
/proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
{'error': 'Proizvod s traženim ID-em ne postoji'} .
Proizvode pohranite u listu rječnika:
"""
import aiohttp
from aiohttp import web
from aiohttp.web import AppRunner
import asyncio

app = web.Application()

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Mis", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slusalice", "cijena": 50}
]

async def fetch_proizvodi(request):
    return web.json_response(proizvodi)

async def fetch_proizvod(request):
    proizvod_id = int(request.match_info["id"])
    for proizvod in proizvodi:
        if proizvod["id"] == proizvod_id:
            return web.json_response(proizvod)
    return web.json_response({'error': 'Proizvod s trazenim ID-em ne postoji'}, status=404)

app.router.add_get("/proizvodi", fetch_proizvodi)
app.router.add_get("/proizvodi/{id}", fetch_proizvod)

async def run_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner=runner, host="localhost", port=8081)
    await site.start()
    
async def main():
    await run_server()
    async with aiohttp.ClientSession() as session: 
        svi_proizvodi = await session.get('http://localhost:8081/proizvodi') 
        print(await svi_proizvodi.text()) 
        proizvod = await session.get('http://localhost:8081/proizvodi/3') 
        print("Proizvod s id-em 3: ", await proizvod.text()) 
        proizvod = await session.get('http://localhost:8081/proizvodi/13') 
        print("Proizvod koji ne postoji: ", await proizvod.text()) 
asyncio.run(main())