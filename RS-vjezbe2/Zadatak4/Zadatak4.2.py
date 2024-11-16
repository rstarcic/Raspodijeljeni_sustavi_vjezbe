"""
Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i
b .
"""
import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        return self.a / self.b

    def potenciranje(self):
        return self.a ** self.b
    
    def korijen(self):
        return math.sqrt(self.a)

kalkulator = Kalkulator(11, 3)

print(f"Zbroj: {kalkulator.zbroj()}")
print(f"Oduzimanje: {kalkulator.oduzimanje()}")
print(f"Množenje: {kalkulator.mnozenje()}")
print(f"Dijeljenje: {kalkulator.dijeljenje()}")
print(f"Potenciranje: {kalkulator.potenciranje()}")
print(f"Korijen: {kalkulator.korijen()}")