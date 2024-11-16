from shop import proizvodi as pr
from shop import narudzbe as nar

# proizvodi 
proizvodi = [
{"naziv": "Laptop", "cijena": 5000, "kolicina": 12},
{"naziv": "Monitor", "cijena": 1000, "kolicina": 2},
{"naziv": "Tipkovnica", "cijena": 200, "kolicina": 5},
{"naziv": "Miš", "cijena": 100, "kolicina": 5}
]
 
for proizvod in proizvodi:
    pr.dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    
for proizvod in pr.proizvodi:
    print(proizvod.ispis())

# narudzba
narudzba = nar.napravi_narudzbu(proizvodi)
if isinstance(narudzba, nar.Narudzba):
    print(narudzba.ispis_narudzbe())  # Naruceni proizvodi: Laptop x 12 Monitor x 2 Tipkovnica x 5 Miš x 5 . Ukupna cijena: 63500
else:
    print(narudzba)  