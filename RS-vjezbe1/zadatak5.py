# 5. zadatak - faktorijel broja koristeći for i while petlje.
# for petlja
broj = int(input("Unesi broj za izračun faktorijela: "))
rezultat = 1

for i in range(1, broj + 1):
    rezultat *= i

print(f"Faktorijel broja {broj} je {rezultat}")

 # while petlja
broj = int(input("Unesi broj za izračun faktorijela: "))
rezultat = 1
i = 1

while(i <= broj ):
    rezultat *= i
    i += 1
    
print(f"Faktorijel broja {broj} je {rezultat}")