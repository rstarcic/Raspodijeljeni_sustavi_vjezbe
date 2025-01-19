from pydantic import BaseModel
from typing import Optional
from datetime import date

class Izdavac(BaseModel):
    naziv: str
    adresa: str
    
class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = date.today().year
    broj_stranica: int
    izdavac: Izdavac
    
izdavac = Izdavac(
    naziv="Nakladnik d.o.o.",
    adresa="Ulica Knjiga 123, Zagreb"
)

knjiga = Knjiga(
    naslov="Programiranje u Pythonu",
    ime_autora="Marko",
    prezime_autora="Marković",
    broj_stranica=350,
    izdavac=izdavac
)

print(knjiga)
