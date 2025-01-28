
from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional

class Movie(BaseModel):
    Title: str
    Year: int = Field(ge=1900)
    Rated: str 
    Released: Optional[str] = "Released date unknown"
    Runtime: str
    Genre: str
    Director: Optional[str] = "Director unknown"
    Writer: str
    Actors: str
    Plot: str 
    Language: str 
    Country: str
    Awards: Optional[str] = "Awards unknown" 
    Poster: Optional[str] = "Poster unknown"
    Metascore: Optional[str] = Field(None) 
    imdbRating: Optional[float] = Field(None, ge=0, le=10) 
    imdbVotes: Optional[int] = Field(None, gt=0) 
    imdbID: Optional[str] = "IMDB id unknown"  
    Type: Literal["movie", "series"]
    Response: str
    Images: list[str]
    
    @field_validator("Year", mode="before")
    def parse_year(cls, value):
        if isinstance(value, str):
            value = value.split("–")[0]  
            value = ''.join(filter(str.isdigit, value))
            if value.isdigit():
                return int(value)
        raise ValueError(f"Invalid year format: {value}")

    @field_validator("imdbRating", mode="before")
    def parse_imdb_rating(cls, value):
        if isinstance(value, str):
            if value == "N/A":
                return None  
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Invalid imdbRating value: {value}")
        return value

    @field_validator("imdbVotes", mode="before")
    def parse_imdb_votes(cls, value):
        if isinstance(value, str):
            if value == "N/A":
                return None  
            return int(value.replace(",", ""))
        return value