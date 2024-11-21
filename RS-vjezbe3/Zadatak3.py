import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

async def autentifikacija(korisnik_info):
    await asyncio.sleep(3)
    korisnik_u_bazi = [korisnik for korisnik in baza_korisnika if korisnik["korisnicko_ime"] == korisnik_info["korisnicko_ime"] and korisnik["email"] == korisnik_info["email"]]
    if korisnik_u_bazi:
        rezultat = await autorizacija(korisnik_info, baza_lozinka)
        return rezultat
    else:
        return f"Korisnik {korisnik_info} nije u bazi."

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]
    
async def autorizacija(korisnik_info, baza_lozinki):
    await asyncio.sleep(2)
    for korisnik in baza_lozinki:
        if(korisnik_info["korisnicko_ime"] == korisnik["korisnicko_ime"] and korisnik_info["lozinka"] == korisnik["lozinka"]):
            return f"Korisnik {korisnik_info}: Autorizacija uspješna." 
    else:
        return f"Korisnik{korisnik_info}: Autorizacija neuspješna."
   
  
korisnik = {"korisnicko_ime": "ana_anic", "email": "aanic@gmail.com", "lozinka": "super_teska_lozinka"}
async def main():
    rezultat = await autentifikacija(korisnik)
    print(rezultat)
    
asyncio.run(main())