#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')

import django
django.setup()

from cinema_app.models import Movie, Cinema, Screening
from datetime import datetime, timedelta
import random

def load_test_data():
    Screening.objects.all().delete()
    Movie.objects.all().delete()
    Cinema.objects.all().delete()
    
    print("Створення кінотеатрів...")

    cinema1 = Cinema.objects.create(
        name="Кіноман",
        ticket_price=150.00,
        seats_count=300,
        address="м. Київ, вул. Хрещатик, 25",
        phone="+380 (44) 123-45-67"
    )
    
    cinema2 = Cinema.objects.create(
        name="Мультиплекс",
        ticket_price=200.00,
        seats_count=500,
        address="м. Київ, вул. Велика Васильківська, 72",
        phone="+380 (44) 234-56-78"
    )
    
    cinema3 = Cinema.objects.create(
        name="Сінема Сіті",
        ticket_price=180.00,
        seats_count=400,
        address="м. Київ, пр-т Перемоги, 136",
        phone="+380 (44) 345-67-89"
    )
    
    print("Створення фільмів...")

    movies_list = [
        {"title": "Іронія долі, або З легким паром!", "genre": "комедія", "duration": 184, "rating": 8.6},
        {"title": "Операція 'И' та інші пригоди Шурика", "genre": "комедія", "duration": 95, "rating": 8.5},
        {"title": "Кавказька полонянка", "genre": "комедія", "duration": 82, "rating": 8.3},
        {"title": "Брильянтова рука", "genre": "комедія", "duration": 100, "rating": 8.7},
        {"title": "Джентельмени удачі", "genre": "комедія", "duration": 84, "rating": 8.6},
        {"title": "Москва сльозам не вірить", "genre": "мелодрама", "duration": 150, "rating": 8.1},
        {"title": "Любов і голуби", "genre": "мелодрама", "duration": 107, "rating": 8.2},
        {"title": "Службовий роман", "genre": "мелодрама", "duration": 159, "rating": 8.4},
        {"title": "Вокзал для двох", "genre": "мелодрама", "duration": 141, "rating": 8.0},
        {"title": "Термінатор 2: Судний день", "genre": "бойовик", "duration": 137, "rating": 8.6},
        {"title": "Матриця", "genre": "бойовик", "duration": 136, "rating": 8.7},
        {"title": "Леон", "genre": "бойовик", "duration": 133, "rating": 8.5},
    ]
    
    movies = []
    for movie_data in movies_list:
        movie = Movie.objects.create(**movie_data)
        movies.append(movie)
    
    print("Створення показів...")
    
    cinemas = [cinema1, cinema2, cinema3]
    today = datetime.now().date()
    
    for i in range(15):
        movie = random.choice(movies)
        cinema = random.choice(cinemas)
        start_date = today + timedelta(days=random.randint(0, 30))
        show_days = random.randint(3, 21)
        
        Screening.objects.create(
            movie=movie,
            cinema=cinema,
            start_date=start_date,
            show_days=show_days
        )
    
    print("\n" + "="*50)
    print("ДАНІ УСПІШНО ЗАВАНТАЖЕНІ!")
    print(f"Кінотеатрів: {Cinema.objects.count()}")
    print(f"Фільмів: {Movie.objects.count()}")
    print(f"Показів: {Screening.objects.count()}")
    print("="*50)

if __name__ == "__main__":
    load_test_data()