import asyncio

async def secure_data(osjetljivi_podaci):
    await asyncio.sleep(3)
    return {
        "prezime": osjetljivi_podaci["prezime"],
        "broj_kartice": hash(str(osjetljivi_podaci["broj_kartice"])),
        "cvv": hash(str(osjetljivi_podaci["cvv"]))
    }

osjetljivi_podaci = [
    {"prezime": "Anic", "broj_kartice": "33244523421", "cvv": 453}, 
    {"prezime": "Jovic", "broj_kartice": "98765432101", "cvv": 321},
    {"prezime": "Kovacevic", "broj_kartice": "12345678910", "cvv": 789}
]

     
async def main(): 
    zadaci = [asyncio.create_task(secure_data(podatak)) for podatak in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)
    print("Rezultati", rezultati)
    for rez in rezultati:
        print(rez)
        
asyncio.run(main())