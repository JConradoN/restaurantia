import sqlite3
import os
import json

def query_db(query):
    db_path = os.path.join(os.path.dirname(__file__), '../db/restaurants.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

def get_restaurants():
    return query_db('SELECT * FROM Restaurants')

def get_restaurant_by_name(name):
    return query_db(f"SELECT * FROM Restaurants WHERE name LIKE '%{name}%'")

def update_database(json_file):
    db_path = os.path.join(os.path.dirname(__file__), '../db/restaurants.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        cursor.execute('''
            INSERT OR REPLACE INTO Restaurants (name, rating, price_range, delivery_time, delivery_fee, distance, category, avatar, url, tags, paymentCodes, minimumOrderValue, regionGroup, catalogGroup, ibge)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            item['name'],
            item['rating'],
            item['price_range'],
            item['delivery_time'],
            item['delivery_fee'],
            item['distance'],
            item['category'],
            item['avatar'],
            item['url'],
            item['tags'],
            item['paymentCodes'],
            item['minimumOrderValue'],
            item['regionGroup'],
            item['catalogGroup'],
            item['ibge']
        ))

    conn.commit()
    conn.close()
