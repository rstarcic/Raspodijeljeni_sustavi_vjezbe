# 1. Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda el: len(el) ** 2, nizovi))
print(kvadrirane_duljine) # [36, 36, 36, 49]

# 2. Koristeći funkciju filter , filtrirajte samo brojeve koji su veći od 5:
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda broj: broj > 5, brojevi))
print(veci_od_5) # [21, 33, 45, 9, 10]

""" 3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu
transform rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi
originalni brojevi, a vrijednosti kvadrati tih brojeva: """
brojevi = [10, 5, 12, 15, 20]
    
transform = dict(map(lambda broj: (broj, broj**2), brojevi))
print(transform) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

# 4. Koristeći funkcije all i map , provjerite jesu li svi studenti punoljetni:
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"] > 18, studenti))
print(svi_punoljetni) # False

""" 5. Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
min_duljina : """

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))

duge_rijeci = list(filter(lambda rijec : len(rijec) > min_duljina, rijeci))
print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']

