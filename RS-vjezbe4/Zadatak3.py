"""
3. Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
URL: https://catfact.ninja/fact .
Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
*cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
zip(dog_facts, cat_facts) .
"""
import asyncio
import aiohttp

async def fetch_dog_facts(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    response_json = await response.json()
   # print(response_json)
    return response_json["data"][0]["attributes"]["body"]

async def fetch_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    response_json = await response.json()
   # print(response_json)
    return response_json["fact"]

async def mix_facts(dog_list, cat_list):
    mix_list = [dog_fact if len(dog_fact) > len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_list, cat_list)]
    # ili
    #mix_list = []
    #for dog_fact, cat_fact in zip(dog_list, cat_list):
    #    if len(dog_fact) > len(cat_fact):
    #        mix_list.append(dog_fact)
    #    else:
    #        mix_list.append(cat_fact)
    return mix_list
    
async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [asyncio.create_task(fetch_dog_facts(session)) for _ in range(5)]
        cat_facts_tasks = [asyncio.create_task(fetch_cat_fact(session)) for _ in range(5)]
        dog_and_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)
        
        dog_facts = dog_and_cat_facts[:5]
        cat_facts = dog_and_cat_facts[5:]
      
        #print(dog_facts)
        #print(cat_facts)
        
        mixed_facts = await mix_facts(dog_facts, cat_facts)

        print("Mixane činjenjice o psima i mačkama:")
        for fact in mixed_facts:
            print(f"- {fact}")
        
        
asyncio.run(main())