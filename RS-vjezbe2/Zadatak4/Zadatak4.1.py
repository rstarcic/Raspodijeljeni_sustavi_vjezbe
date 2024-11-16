"""
Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
Dodajte metodu ispis koja će ispisivati sve atribute automobila.
Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
godine dohvatite pomoću datetime modula.
"""
import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
        
    def ispis(self):
        return (
            f"Marka: {self.marka}\n"
            f"Model: {self.model}\n"
            f"Godina proizvodnje: {self.godina_proizvodnje}\n"
            f"Kilometraža: {self.kilometraza}"
        )
        
    def starost(self):
        starost_auta = datetime.datetime.now().year - self.godina_proizvodnje
        return f"Starost automobila: {starost_auta}" 

auto = Automobil("MINI", "Cooper", 2010, 180000)  
print(auto.ispis())
print(auto.starost())