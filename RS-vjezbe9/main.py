from fastapi import FastAPI, HTTPException, Query
from models import Automobil, ResponseCar, CreateCar

app = FastAPI()

automobili = [
    {"id": 1, "marka": "Toyota", "model": "Corolla", "godina_proizvodnje": 2020, "cijena": 20000.0, "boja": "Crna"},
    {"id": 2, "marka": "Volkswagen", "model": "Golf", "godina_proizvodnje": 2019, "cijena": 18000.0, "boja": "Bijela"},
    {"id": 3, "marka": "BMW", "model": "X5", "godina_proizvodnje": 2021, "cijena": 50000.0, "boja": "Plava"},
    {"id": 4, "marka": "Audi", "model": "A4", "godina_proizvodnje": 2022, "cijena": 45000.0, "boja": "Siva"},
    {"id": 5, "marka": "Mercedes", "model": "C-Class", "godina_proizvodnje": 2021, "cijena": 55000.0, "boja": "Crvena"}
]

# zadatak 1.
"""
@app.get("/automobili/{id}", response_model=Automobil)
def get_automobil(id: int):
    for automobil in automobili:
        if automobil["id"] == id:
            return automobil
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")
"""

# zadatak 2.
@app.get("/automobili/{id}", response_model=Automobil)
def get_automobil(
    id: int, min_cijena: float = Query(1,gt=0, description="Minimalna cijena automobila"), 
    max_cijena: float = Query(description="Maksimalna cijena automobila"), 
    min_godina: int = Query(1961, gt=1960, description="Minimalna godina proizvodnje automobila"), 
    max_godina: int = Query(description="Maksimalna godina proizvodnje automobila")
    ):
    
    if min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena ne može biti veća od maksimalne cijene")
  
    if min_godina > max_godina:
        raise HTTPException(status_code=400, detail="Minimalna godina ne može biti veća od maksimalne godine")
    
    for automobil in automobili:
        if automobil["id"] == id:
            if min_cijena <= automobil["cijena"] <= max_cijena and min_godina <= automobil["godina_proizvodnje"] <= max_godina:
                return automobil
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

# zadatak 3.
@app.post("/automobili", response_model=ResponseCar)
def add_automobil(automobil: CreateCar):
    for dostupan_automobil in automobili:
        if dostupan_automobil["marka"] == automobil.marka and  dostupan_automobil["model"] == automobil.model and dostupan_automobil["boja"] == automobil.boja and dostupan_automobil["godina_proizvodnje"] == automobil.godina_proizvodnje:
            raise HTTPException(status_code=404, detail="Automobil već postoji u bazi podataka")
        
    new_id = len(automobili) + 1
    cijena_pdv = automobil.cijena * 1.25
    novi_automobil : ResponseCar = { "id": new_id, **automobil.model_dump(), "cijena_pdv": cijena_pdv}
    automobili.append(novi_automobil)
    
    print(automobili)
    return novi_automobil
