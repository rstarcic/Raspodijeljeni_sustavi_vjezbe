class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena
    
    def ispis_narudzbe(self):
        ispis_proizvoda = ""
        for kupljeni_proizvod in self.proizvodi:
            ispis_proizvoda += f"{kupljeni_proizvod["naziv"]} x {kupljeni_proizvod["kolicina"]} "
        return f"Naruceni proizvodi: {ispis_proizvoda}. Ukupna cijena: {self.ukupna_cijena}"
        

def napravi_narudzbu(proizvodi):
    ukupna_cijena = 0
    narudzbe = list()
    if not isinstance(proizvodi, list):
        return "Argument proizvodi mora biti lista"
    if not proizvodi:
        return "Lista ne smije biti prazna"
    for proizvod in proizvodi:
        if not isinstance(proizvod, dict):
            return "Element liste mora biti dictionary"
        if not all(key in proizvod for key in ["naziv", "cijena", "kolicina"]):
            return "Svaki dict mora sadržavati ključeve naziv, cijena i kolicina."
        if proizvod["kolicina"] == 0:
            return f"Proizvod {proizvod["naziv"]} nije dostupan"
        else:
            ukupna_cijena += proizvod["cijena"] * proizvod["kolicina"]
    narudzba = Narudzba(proizvodi, ukupna_cijena)
    narudzbe.append(narudzba)
    return narudzba