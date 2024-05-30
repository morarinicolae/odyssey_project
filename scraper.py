import requests
from bs4 import BeautifulSoup

def extract_movie_data_for_year(year: int) -> list:
    """Fetch the most popular movies in a given year."""
    url = f'https://www.google.com/search?q=popular+movies+in+{year}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemplu de scraping (poate varia în funcție de structura paginii)
    movies = []
    for result in soup.select('.BNeawe .s3v9rd'):
        movie = {
            'name': result.get_text(),  # trebuie ajustat pentru a extrage corect numele
            'duration': 'Unknown',  # trebuie găsită metoda pentru a extrage durata
            'type': 'Unknown',  # trebuie găsită metoda pentru a extrage tipul
            'genre': 'Unknown'  # trebuie găsită metoda pentru a extrage genul
        }
        movies.append(movie)

    return movies
