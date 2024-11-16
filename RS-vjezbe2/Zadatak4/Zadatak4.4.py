"""
Definirajte klasu Krug s atributom r . Dodajte metode opseg i povrsina koje će računati opseg i
površinu kruga.
Stvorite objekt klase Krug s proizvoljnim radijusom i ispišite opseg i površinu kruga.
"""
import math
class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        return f"Opseg kruga: {2 * self.r * math.pi}"
    
    def povrsina(self):
        return f"Povrsina kruga: {self.r **2 * math.pi}"

krug = Krug(4)
print(krug.opseg())
print(krug.povrsina())    