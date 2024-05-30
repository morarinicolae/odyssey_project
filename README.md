# Odyssey Project

*Movie Info Scraper*

## Project Description

*The Odyssey project is a FastAPI application that extracts and stores information about popular movies in a specific year from the internet. This application utilizes web scraping techniques to fetch movie data and stores it in a JSON file. Additionally, it provides an API for interacting with this data, allowing users to get information about movies, add new movies, and update or delete existing movies.
*

## Installation

1. Clonați repository-ul:
    ```bash
    git clone https://github.com/exemplu/movie-info-scraper.git
    cd movie-info-scraper
    ```

2. Instalați dependențele:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Rulați scriptul de scraping pentru a obține datele:
    ```bash
    python scraper.py
    ```

2. Porniți serverul Flask:
    ```bash
    python app.py
    ```


## Testing

1. Rulați testele:
    ```bash
    python -m unittest test_data_processing.py
    ```

