"""  
Definirajte novu FastAPI rutu GET /filmovi koja će klijentu vraćati listu filmova definiranu u sljedećoj
listi:
"""
from fastapi import FastAPI
from models import Film, CreateFilm
from typing import Optional

app = FastAPI()

filmovi = [
 {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
 {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
 {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
 {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi", response_model=list[Film])
def get_movies(genre: Optional[str]=None, min_godina: Optional[int]=2000):
    if genre or min_godina:
        filtered_movies = [film for film in filmovi if film["genre"] == genre and film["godina"] >= min_godina]
    return filtered_movies

@app.get("/filmovi/{id}", response_model=Film)
def get_movie_by_id(id: int):
    movie = next((film for film in filmovi if film["id"] == id), None)
    return movie

@app.post("/filmovi")
def add_new_movie(film: CreateFilm):
    id = len(filmovi) + 1
    new_movie = Film(id=id, **film.model_dump())
    filmovi.append(new_movie)
    return new_movie