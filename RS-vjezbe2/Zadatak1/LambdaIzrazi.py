# 1. kvadriranje broja
kvadrat_broja = lambda x : x**2
print(kvadrat_broja(7)) 

# 2. zbroji pa kvadriraj
zbroji_i_kvadriraj = lambda x, y : (x + y) ** 2
print(zbroji_i_kvadriraj(2,4))

# 3. kvadriraj duljinu niza
kvadriraj_duljinu = lambda niz : len(niz) ** 2
print(kvadriraj_duljinu("informatika"))

# 4. pomnoži vrijednosti s 5 pa potenciraj na x
pomnozi_i_potenciraj = lambda x, y : (y * 5) ** x
print(pomnozi_i_potenciraj(3, 5))

# 5. vrati True ako je broj paran, inače vrati None
paran_broj = lambda x : True if x % 2 == 0 else None
print(paran_broj(6))
print(paran_broj(7))