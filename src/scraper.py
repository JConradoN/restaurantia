# scraper.py
import requests
from bs4 import BeautifulSoup
import sqlite3

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract desired data here
    restaurants = []
    for item in soup.find_all('div', class_='restaurant'):
        name = item.find('h2').text
        menu = item.find('p', class_='menu').text
        rating = item.find('span', class_='rating').text
        reviews = item.find('div', class_='reviews').text
        restaurants.append((name, menu, rating, reviews))
    return restaurants

def save_to_db(data):
    conn = sqlite3.connect('db/restaurants.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            menu TEXT,
            rating TEXT,
            reviews TEXT
        )
    ''')
    cur.executemany('INSERT INTO Restaurants (name, menu, rating, reviews) VALUES (?, ?, ?, ?)', data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    url = 'https://ifood.com.br'
    data = scrape_website(url)
    save_to_db(data)
    print("Data scraped and saved to database.")