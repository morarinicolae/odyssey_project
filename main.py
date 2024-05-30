from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre
from scraper import extract_movie_data_for_year
import os

app = FastAPI()
DATA_FILE = os.path.join('data_storage', 'movies.json')

def load_movies() -> Dict[int, List[Dict]]:
    try:
        with open(DATA_FILE, 'r') as file:
            movies = json.load(file)
            return movies
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_movies(movies: Dict[int, List[Dict]]):
    with open(DATA_FILE, 'w') as file:
        json.dump(movies, file, indent=4)

def fetch_movie_data_for_year(year: int) -> List[Dict]:
    entries = extract_movie_data_for_year(year)
    movies = []

    for entry in entries:
        movie_type = extract_movie_type(entry)
        name = extract_name(entry, movie_type)
        duration = extract_duration_period(entry)[2]
        genre = extract_genre(entry)

        movie = {
            "name": name,
            "duration": duration,
            "type": movie_type,
            "genre": genre
        }
        movies.append(movie)

    return movies

@app.get("/", response_model=Dict[str, str])
def read_root():
    return {"message": "Welcome to the Movie API!"}

@app.get("/movies", response_model=Dict[int, List[Dict]])
def get_movies() -> Dict[int, List[Dict]]:
    return load_movies()

@app.get("/movies/{year}", response_model=List[Dict])
def get_movies_by_year(year: int) -> List[Dict]:
    movies = load_movies()
    if year in movies:
        return movies[year]
    raise HTTPException(status_code=404, detail="Movies for the specified year not found")

@app.post("/movies/{year}", response_model=List[Dict])
def add_movies_by_year(year: int) -> List[Dict]:
    movies = load_movies()
    if year in movies:
        raise HTTPException(status_code=400, detail="Movies for the specified year already exist")

    new_movies = fetch_movie_data_for_year(year)
    movies[year] = new_movies
    save_movies(movies)
    return new_movies

@app.put("/movies/{year}", response_model=List[Dict])
def update_movie(year: int) -> List[Dict]:
    movies = load_movies()
    new_movies = fetch_movie_data_for_year(year)
    movies[year] = new_movies
    save_movies(movies)
    return new_movies

@app.delete("/movies/{year}/{name}", response_model=Dict)
def delete_movie(year: int, name: str) -> Dict:
    movies = load_movies()
    if year in movies:
        for movie in movies[year]:
            if movie["name"].lower() == name.lower():
                movies[year].remove(movie)
                save_movies(movies)
                return movie
        raise HTTPException(status_code=404, detail="Movie not found")
    raise HTTPException(status_code=404, detail="Movies for the specified year not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)  # You can access the API docs at http://localhost:8000/docs
