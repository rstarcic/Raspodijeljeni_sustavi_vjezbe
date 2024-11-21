import asyncio
import random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        print(f"Broj {broj} je paran")
    else:
        print(f"Broj {broj} nije paran")
        
async def main(): 
    lista = [random.randint(1, 100) for _ in range(1,11)]
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in lista]
    print(lista)
    print(zadaci)
    rezultati = await asyncio.gather(*zadaci)
    
    for rez in rezultati:
        print(rez)
asyncio.run(main())