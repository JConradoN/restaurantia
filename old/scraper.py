# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extraia os dados desejados aqui
    data = soup.find_all('p')
    return [p.text for p in data]

if __name__ == "__main__":
    url = 'https://ifood.com.br'
    data = scrape_website(url)
    print(data)