from fastapi import FastAPI, HTTPException
import json
from typing import List, Dict
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre
from scraper import fetch_movie_data_for_year

app = FastAPI()
DATA_FILE = 'movies.json'

def load_movies() -> Dict[int, List[Dict]]:
    """Load the movie data from a JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    try:
        with open(DATA_FILE, 'r') as file:
            movies = json.load(file)
            return movies
    except FileNotFoundError:
        return {}

def save_movies(movies: Dict[int, List[Dict]]):
    """Save the movie data to a JSON file.

    Args:
        movies (Dict[int, List[Dict]]): The movie data to save.
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(movies, file, indent=4)

@app.get("/movies", response_model=Dict[int, List[Dict]])
def get_movies() -> Dict[int, List[Dict]]:
    """Retrieve all movies from the JSON file.

    Returns:
        Dict[int, List[Dict]]: The movie data with years as keys and lists of movies as values.
    """
    return load_movies()

@app.get("/movies/{year}", response_model=List[Dict])
def get_movies_by_year(year: int) -> List[Dict]]:
    """Retrieve movies for a specific year from the JSON file.

    Args:
        year (int): The year for which to retrieve movies.

    Returns:
        List[Dict]: A list of movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year are not found.
    """
    movies = load_movies()
    if year in movies:
        return movies[year]
    raise HTTPException(status_code=404, detail="Movies for the specified year not found")

@app.post("/movies/{year}", response_model=List[Dict])
def add_movies_by_year(year: int) -> List[Dict]]:
    """Fetch and add movies for a specific year to the JSON file.

    Args:
        year (int): The year for which to fetch and add movies.

    Returns:
        List[Dict]: A list of newly added movies for the specified year.

    Raises:
        HTTPException: If movies for the specified year already exist.
    """
    movies = load_movies()
    if year in movies:
        raise HTTPException(status_code=400, detail="Movies for the specified year already exist")

    new_movies = fetch_movie_data_for_year(year)
    movies[year] = new_movies
    save_movies(movies)
    return new_movies

@app.put("/movies/{year}", response_model=List[Dict]])
def update_movie(year: int) -> List[Dict]]:
    """Update movies for a specific year in the JSON file.

    Args:
        year (int): The year for which to update movies.

    Returns:
        List[Dict]: A list of updated movies for the specified year.
    """
    movies = load_movies()
    new_movies = fetch_movie_data_for_year(year)
    movies[year] = new_movies
    save_movies(movies)
    return new_movies

@app.delete("/movies/{year}/{name}", response_model=Dict)
def delete_movie(year: int, name: str) -> Dict:
    """Delete a movie for a specific year from the JSON file.

    Args:
        year (int): The year of the movie to delete.
        name (str): The name of the movie to delete.

    Returns:
        Dict: The deleted movie's details.

    Raises:
        HTTPException: If the movie for the specified year and name is not found.
    """
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
    uvicorn.run(app, host="0.0.0.0", port=8000)  # You can access the API docs at http://localhost:8000/docs
