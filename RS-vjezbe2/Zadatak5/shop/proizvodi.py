class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina
    
    def ispis(self):
        return (
            f"Naziv: {self.naziv} \n"
            f"Cijena: {self.cijena} \n"
            f"Kolicina: {self.kolicina} \n"
        )
        
proizvod1 = Proizvod("Laptop HP Victus", 1200, 10)
proizvod2 = Proizvod("Gaming slušalice", 50, 3)
proizvodi = [proizvod1, proizvod2]

def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(novi_proizvod)