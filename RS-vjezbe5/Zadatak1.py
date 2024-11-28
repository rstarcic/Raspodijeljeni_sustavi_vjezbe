"""
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.
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

app.router.add_get("/proizvodi", fetch_proizvodi)

web.run_app(app, host="localhost", port=8080)