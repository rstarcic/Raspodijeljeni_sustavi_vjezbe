import aiohttp
import asyncio

async def fetch_service1():
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get('http://localhost:8081/pozdrav')
        return await rezultat.json()

async def fetch_service2():
    async with aiohttp.ClientSession() as session:
        rezultat = await session.get('http://localhost:8082/pozdrav')
        return await rezultat.json()


async def main():
    print("Pokrećem main korutinu")
    result = await asyncio.gather(fetch_service1(), fetch_service2())
    print("Konkurentno:" , result)
    """
    service1_response = await fetch_service1()
    print(f"Odgovor mikroservisa 1: {service1_response}")
    service2_response = await fetch_service2()
    print(f"Odgovor mikroservisa 2: {service2_response}")
    print(service1_response, service2_response)
"""
asyncio.run(main())