from pydantic import BaseModel

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str
    
class CreateCar(BaseCar):
    pass

class ResponseCar(BaseCar):
    id: int
    cijena_pdv: float