"""
Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
"Radim na poziciji {pozicija}".
Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
povećava plaću radnika ( Radnik ) za iznos povecanje .
Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i
give_raise .
"""

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    
    def work(self):
        return f"Radim na poziciji {self.pozicija}."
    
class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
        
    def work(self):
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}."
    
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        return f"Plaća radnika {radnik.ime} sada iznosi {radnik.placa}."

radnik = Radnik("Ivan", "Software Engineer", 1300)
menadzer = Manager("Marko", "Menadžer", 1400, "IT")

print(radnik.work())
print(menadzer.work())
print(menadzer.give_raise(radnik, 200))
