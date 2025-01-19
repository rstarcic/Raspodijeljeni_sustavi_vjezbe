from pydantic import BaseModel
from typing import TypedDict

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class StolInfo(TypedDict):
    broj: int
    lokacija: str

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: list[Jelo]
    ukupna_cijena: float

stol = {"broj": 5, "lokacija": "terasa"}
jela = [
    Jelo(id=1, naziv="pizza margherita", cijena=7.99),
    Jelo(id=4, naziv="pizza calzone", cijena=9.99)
]

naruzdba = RestaurantOrder(id=12, ime_kupca="Lara", stol_info=stol, jela=jela, ukupna_cijena=sum(jelo.cijena for jelo in jela))
print(naruzdba)