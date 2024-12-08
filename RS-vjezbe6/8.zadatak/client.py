import asyncio
import aiohttp

async def fetch_cat_facts(amount):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"http://localhost:8086/cat/{amount}")
        return await response.json()
    
async def fetch_filtered_facts(fact_list):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://localhost:8087/facts", json={"facts": fact_list})
        return await response.json()


async def main():
    amount = 10
    facts = await fetch_cat_facts(amount)
    fact_list = facts["facts"]
    filtered_facts = await fetch_filtered_facts(fact_list)
    print("Filtered facts:", filtered_facts)
    
asyncio.run(main())