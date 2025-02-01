from pydantic import BaseModel, Field
from datetime import datetime as timestamp

class BaseObjava(BaseModel):
    korisnik: str = Field(max_length=20, description="Korisničko ime autora objave")
    tekst: str = Field(max_length=280, description="Tekst objave")

class RequestObjava(BaseObjava):
    pass

class ResponseObjava(BaseObjava):
    id: int
    vrijeme: timestamp  
    
class AuthKorisnikRequest(BaseModel):
    korisnicko_ime: str
    lozinka: str