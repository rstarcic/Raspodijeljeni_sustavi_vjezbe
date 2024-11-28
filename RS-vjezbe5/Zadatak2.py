"""
Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji /proizvodi prima POST zahtjeve
s podacima o proizvodu. Podaci se šalju u JSON formatu i sadrže ključeve naziv , cijena i količina .
Handler funkcija treba ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i vratiti
odgovor s novom listom proizvoda u JSON formatu.
"""
from aiohttp import web

app = web.Application()

proizvodi = [
    {"naziv": "Mlijeko", "cijena": 5.5, "kolicina": 5},
    {"naziv": "Skittles", "cijena": 2.5, "kolicina": 1},
    {"naziv": "Banane", "cijena": 5.5, "kolicina": 5}
]

async def fetch_proizvodi(request):
    print("Request received")
    return web.json_response(proizvodi)

async def create_proizvod(request):
    data = await request.json()
    naziv = data.get("naziv")
    cijena = data.get("cijena")
    kolicina = data.get("kolicina")
    
    print(f"Naziv: {naziv} Cijena: {cijena} Količina: {kolicina}")
    novi_proizvod = {"naziv": naziv, "cijena": cijena, "kolicina": kolicina}

    proizvodi.append(novi_proizvod)
    
    return web.json_response(proizvodi)

app.router.add_get("/proizvodi", fetch_proizvodi)
app.router.add_post("/proizvodi", create_proizvod )

web.run_app(app, host="localhost", port=8080)