# 3. zadatak - pogađanje broja
import random

broj = random.randint(1, 100)
broj_pogoden = False
broj_pokusaja = 0

while(not broj_pogoden):
    uneseni_broj = int(input("Unesi i pogodi broj između 1 i 100: "))
    broj_pokusaja += 1
    
    if uneseni_broj < broj:
        print("Uneseni broj je manji od ciljanog.")
    elif uneseni_broj > broj:
        print("Uneseni broj je veći od ciljanog.")
    else:
        broj_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")
