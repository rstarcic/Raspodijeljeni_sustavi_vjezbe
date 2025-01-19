from pydantic import BaseModel
from typing import Literal, List

class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "azuriranje", "citanje"]] = []

admin = Admin(ime="Marko", prezime="Markovic", korisnicko_ime="marko_23", email="marko@gmail.com", ovlasti=["brisanje", "azuriranje"])
print(admin)

admin_bez_ovlasti = admin = Admin(ime="Pero", prezime="Peric", korisnicko_ime="pero_23", email="pero@gmail.com")
print(admin_bez_ovlasti)