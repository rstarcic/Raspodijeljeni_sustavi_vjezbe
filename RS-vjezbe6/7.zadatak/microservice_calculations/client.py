import asyncio
import aiohttp

async def service_zbroj(brojevi):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://localhost:8083/zbroj", json=brojevi)
        return await response.json()
    
async def service_umnozak(brojevi):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://localhost:8084/umnozak", json=brojevi)
        return await response.json()

async def service_kolicnik(zbroj, umnozak):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://localhost:8085/kolicnik", json={"zbroj":zbroj, "umnozak":umnozak})
        return await response.json()
    
async def main():
    print("Pokrećem main korutinu")
    async with aiohttp.ClientSession() as session:
        brojevi = {"brojevi": [1,2,3,4]}
        zbroj_result, umnozak_result = await asyncio.gather(service_zbroj(brojevi), service_umnozak(brojevi))     
        print("Zbroj: ", zbroj_result)
        print("Umnozak: ", umnozak_result)
        kolicnik_result = await service_kolicnik(zbroj_result["zbroj"], umnozak_result["umnozak"])
        print("Kolicnik: ", kolicnik_result)
    
asyncio.run(main())