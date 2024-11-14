# Pomnozi i potenciraj
pomnozi_i_potenciraj = lambda x, y : y * 5 ** x
print(pomnozi_i_potenciraj(3,4))

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda student: student["godine"] > 18, studenti))
print(svi_punoljetni)

lista_rjecnika = [{i : i} if i % 2 == 0 else {i: i**3} for i in range(1,11)]
print(lista_rjecnika)
