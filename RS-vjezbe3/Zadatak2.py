import asyncio

korisnici = [{"ime" : "Ana", "prezime": "Anic"},{"ime" : "Ana", "prezime": "Maric"}]

proizvodi = [{"naziv" : "Montitor", "cijena": 1000},{"naziv" : "Slušalice", "cijena": 50}]

async def korutina_1():
    await asyncio.sleep(3)
    return korisnici

async def korutina_2():
    await asyncio.sleep(5)
    return proizvodi

async def main():
    podaci1, podaci2 = await asyncio.gather(korutina_1(),korutina_2())
    print(f"Podaci1: {podaci1}")
    print(f"Podaci2: {podaci2}")   

asyncio.run(main())
