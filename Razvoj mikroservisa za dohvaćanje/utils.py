import os
import json
from models.Movie import Movie
from typing import List

def load_movies_from_json() -> List[Movie]:
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path_file = os.path.join(base_dir, "data", "movies.json")

        with open(json_path_file, "r", encoding="utf-8") as file:
            movies_data = json.load(file)
            
        return [Movie(**movie) for movie in movies_data]
    except FileNotFoundError:
        raise FileNotFoundError(f"Datoteka '{json_path_file}' nije pronađena.")

