""" 
2. Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).
"""
import asyncio
import aiohttp

async def fetch_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    response_json = await response.json()
   # print(response_json)
    return response_json

async def filter_cat_facts(cat_list_fact):
    cat_list = [fact["fact"] for fact in cat_list_fact if "cat" or "cats" or "Cat" or "Cats" in fact]
    return cat_list

async def main():
    async with aiohttp.ClientSession() as session:
        cat_facts_tasks = [asyncio.create_task(fetch_cat_fact(session)) for _ in range(20)]
        cat_facts = await asyncio.gather(*cat_facts_tasks)

        filtered_facts = await filter_cat_facts(cat_facts)
        for fact in filtered_facts:
            print(f"- {fact}")

asyncio.run(main())