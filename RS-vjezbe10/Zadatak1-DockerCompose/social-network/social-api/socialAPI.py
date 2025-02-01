from fastapi import FastAPI, HTTPException
from models import ResponseObjava, RequestObjava, AuthKorisnikRequest
from datetime import datetime
import aiohttp

app = FastAPI()

objave=[]

@app.post("/objava", response_model=ResponseObjava)
def create_objava(objava: RequestObjava):
    new_id = len(objave) + 1
    current_datetime = datetime.now()
    nova_objava: ResponseObjava = {**objava.model_dump(), "id": new_id, "vrijeme": current_datetime}
    objave.append(nova_objava)
    return nova_objava    

@app.get("/objava/{id}", response_model=ResponseObjava)
def get_objava_by_id(id: int):
    objava = next((objava for objava in objave if objava["id"] == id), None)
    if objava is None:
        raise HTTPException(status_code=400, detail="Ne postoji objava s tim ID-em")
    return objava

async def is_authenticated(auth_podaci: AuthKorisnikRequest):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://auth-api:9000/login", json=auth_podaci.model_dump())
        if response.status != 200:
            return False
        data = await response.json()
        return data.get("authorized")
    
@app.post("/korisnici/{korisnik}/objave", response_model=list[ResponseObjava])
async def get_objava_by_id(korisnik: str, auth_podaci: AuthKorisnikRequest):
    user_authenticated = await is_authenticated(auth_podaci)
    if not user_authenticated:
        raise HTTPException(status_code=401, detail="Neispravno korisničko ime ili lozinka")
    objave_korisnika = [objava for objava in objave if objava["korisnik"] == korisnik]
    if not objave_korisnika:
        raise HTTPException(status_code=400, detail="Ne postoje objave tog korisnika")
    return objave_korisnika
