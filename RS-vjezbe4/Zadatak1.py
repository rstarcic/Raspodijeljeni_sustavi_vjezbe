"""
Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.
"""
import time 
import asyncio
import aiohttp

async def fetch_users(session, i):
    print(f"Šaljem {i}-ti zahtjev")
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    response_json = await response.json()
    #print(response_json)
    return response_json


async def main():
    async with aiohttp.ClientSession() as session:
        zahtjevi = [fetch_users(session, i) for i in range(5)]
        rezultati = await asyncio.gather(*zahtjevi)

        imena = [korisnik["name"] for korisnik in rezultati[0]]
        mailovi = [korisnik["email"] for korisnik in rezultati[0]]
        usernames = [korisnik["username"] for korisnik in rezultati[0]]
        print(imena, mailovi, usernames)
        return rezultati

asyncio.run(main())