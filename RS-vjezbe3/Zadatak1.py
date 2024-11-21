import asyncio

async def korutina():  
    podaci = [i for i in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni")
    return podaci
    
asyncio.run(korutina())