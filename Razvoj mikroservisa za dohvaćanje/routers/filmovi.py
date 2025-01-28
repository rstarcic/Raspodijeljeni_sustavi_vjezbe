from fastapi import APIRouter, HTTPException, Query
from models.Movie import Movie
from utils import load_movies_from_json

router = APIRouter(prefix="/movies")

movies = load_movies_from_json()

@router.get("/", response_model=list[Movie])
def get_movies(   
    min_year: int = Query(description="Minimum year (>= 1900)"),
    max_year: int = Query(description="Maximum year (>= 1900)"),
    min_rating: float = Query(None, ge=0, le=10, description="Minimum IMDb rating (0-10)"),
    max_rating: float = Query(None, ge=0, le=10, description="Maximum IMDb rating (0-10)"),
    type: str = Query(None, description="Type of movie ('movie', 'series')")
):
    filtered_movies = movies

    if min_year is not None:
        filtered_movies = [movie for movie in filtered_movies if movie.Year >= min_year]

    if max_year is not None:
        filtered_movies = [movie for movie in filtered_movies if movie.Year <= max_year]

    if min_rating is not None:
        filtered_movies = [movie for movie in filtered_movies if movie.imdbRating is not None and movie.imdbRating >= min_rating]

    if max_rating is not None:
        filtered_movies = [movie for movie in filtered_movies if movie.imdbRating is not None and movie.imdbRating <= max_rating]

    if type is not None:
        filtered_movies = [movie for movie in filtered_movies if movie.Type == type]

    return filtered_movies

@router.get("/{id}", response_model=Movie)
def get_movie_by_id(id: str):
    movie = next((movie for movie in movies if movie.imdbID == id), None)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with imdb id {id} does not exist")
    return movie    

@router.get("/title/{title}", response_model=Movie)
def get_movie_by_title(title: str):
    movie = next((movie for movie in movies if movie.Title.lower() == title.lower()), None)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with title {title} does not exist")
    return movie    
