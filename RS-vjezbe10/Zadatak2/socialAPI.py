from fastapi import FastAPI, HTTPException
from models import ResponseObjava, RequestObjava
from datetime import datetime

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

@app.get("/korisnici/{korisnik}/objave", response_model=list[ResponseObjava])
def get_objava_by_id(korisnik: str):
    objave_korisnika = [objava for objava in objave if objava["korisnik"] == korisnik]
    if not objave_korisnika:
        raise HTTPException(status_code=400, detail="Ne postoje objave tog korisnika")
    return objave_korisnika

# docker
# docker build -t social-api:1.0 .
# docker run -p 3500:8000 --name social-api social-api:1.0