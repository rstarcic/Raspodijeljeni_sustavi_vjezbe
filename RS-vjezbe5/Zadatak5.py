"""
Nadogradnja 4. zadatka
Nadogradite poslužitelj iz prethodnog zadatka na način da podržava i POST metodu na putanji /narudzbe .
Ova ruta prima JSON podatke o novoj narudžbu u sljedećem obliku. Za početak predstavite da je svaka
narudžba jednostavna i sadrži samo jedan proizvod i naručenu količinu:
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

narudzbe = []

async def create_narudzba(request):
    data_narudzba = await request.json()
    if any(proizvod["id"] == data_narudzba["proizvod_id"] for proizvod in proizvodi):
        narudzbe.append(data_narudzba)        
        return web.json_response(narudzbe, status=201)
    else: 
        return web.json_response({'error': 'Proizvod s traženim ID-em nepostoji'}, status=404)

app.router.add_get("/proizvodi", fetch_proizvodi)
app.router.add_get("/proizvodi/{id}", fetch_proizvod)
app.router.add_post("/narudzbe", create_narudzba)

async def run_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner=runner, host="localhost", port=8081)
    await site.start()
    
async def main():
    await run_server()
    async with aiohttp.ClientSession() as session: 
        svi_proizvodi = await session.get('http://localhost:8081/proizvodi') 
        print("Svi proizvodi: ", await svi_proizvodi.text()) 
        proizvod = await session.get('http://localhost:8081/proizvodi/3') 
        print("Proizvod s id-em 3: ", await proizvod.text()) 
        proizvod = await session.get('http://localhost:8081/proizvodi/13') 
        print("Proizvod koji ne postoji: ", await proizvod.text()) 
        
        nova_narudzba = { "proizvod_id": 1, "kolicina": 2 }
        narudzba = await session.post('http://localhost:8081/narudzbe', json=nova_narudzba)
        print("Nova narudzba ", await narudzba.text()) 
asyncio.run(main())