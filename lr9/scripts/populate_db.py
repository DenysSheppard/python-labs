import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
from create_db import create_connection

fake = Faker('uk_UA')

def clear_tables(conn):
    """Очищення таблиць"""
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM screenings")
        cur.execute("DELETE FROM movies")
        cur.execute("DELETE FROM cinemas")
        conn.commit()
        cur.close()
        print("Таблиці очищені!")
    except Exception as e:
        print(f"Помилка при очищенні таблиць: {e}")
        conn.rollback()

def populate_cinemas(conn):
    """Заповнення таблиці кінотеатрів"""
    cinemas_data = [
        ("Кіноман", 150.00, 300, "м. Київ, вул. Хрещатик, 25", "+380 (44) 123-45-67"),
        ("Мультиплекс", 200.00, 500, "м. Київ, вул. Велика Васильківська, 72", "+380 (44) 234-56-78"),
        ("Сінема Сіті", 180.00, 400, "м. Київ, пр-т Перемоги, 136", "+380 (44) 345-67-89"),
    ]
    
    try:
        cur = conn.cursor()
        for cinema in cinemas_data:
            cur.execute(
                "INSERT INTO cinemas (name, ticket_price, seats_count, address, phone) VALUES (%s, %s, %s, %s, %s)",
                cinema
            )
        conn.commit()
        cur.close()
        print("Дані кінотеатрів додано!")
    except Exception as e:
        print(f"Помилка при заповненні кінотеатрів: {e}")
        conn.rollback()

def populate_movies(conn):
    """Заповнення таблиці фільмів"""
    movies_data = [
        # Комедії
        ("Іронія долі, або З легким паром!", "комедія", 184, 8.6),
        ("Операція 'И' та інші пригоди Шурика", "комедія", 95, 8.5),
        ("Кавказька полонянка", "комедія", 82, 8.3),
        ("Брильянтова рука", "комедія", 100, 8.7),
        ("Джентельмени удачі", "комедія", 84, 8.6),
        
        # Мелодрами
        ("Москва сльозам не вірить", "мелодрама", 150, 8.1),
        ("Любов і голуби", "мелодрама", 107, 8.2),
        ("Службовий роман", "мелодрама", 159, 8.4),
        ("Вокзал для двох", "мелодрама", 141, 8.0),
        
        # Бойовики
        ("Термінатор 2: Судний день", "бойовик", 137, 8.6),
        ("Матриця", "бойовик", 136, 8.7),
        ("Леон", "бойовик", 133, 8.5),
    ]
    
    try:
        cur = conn.cursor()
        for movie in movies_data:
            cur.execute(
                "INSERT INTO movies (title, genre, duration, rating) VALUES (%s, %s, %s, %s)",
                movie
            )
        conn.commit()
        cur.close()
        print("Дані фільмів додано!")
    except Exception as e:
        print(f"Помилка при заповненні фільмів: {e}")
        conn.rollback()

def populate_screenings(conn):
    """Заповнення таблиці транслювання"""
    try:
        cur = conn.cursor()
        
        # Отримуємо всі фільми та кінотеатри
        cur.execute("SELECT movie_id FROM movies")
        movie_ids = [row[0] for row in cur.fetchall()]
        
        cur.execute("SELECT cinema_id FROM cinemas")
        cinema_ids = [row[0] for row in cur.fetchall()]
        
        # Генеруємо 15 показів
        screenings_data = []
        start_date = datetime.now().date()
        
        for i in range(15):
            movie_id = random.choice(movie_ids)
            cinema_id = random.choice(cinema_ids)
            show_start = start_date + timedelta(days=random.randint(0, 30))
            show_days = random.randint(3, 21)
            
            screenings_data.append((movie_id, cinema_id, show_start, show_days))
        
        for screening in screenings_data:
            cur.execute(
                "INSERT INTO screenings (movie_id, cinema_id, start_date, show_days) VALUES (%s, %s, %s, %s)",
                screening
            )
        
        conn.commit()
        cur.close()
        print("Дані транслювання додано!")
    except Exception as e:
        print(f"Помилка при заповненні транслювання: {e}")
        conn.rollback()

def main():
    conn = create_connection()
    if conn is not None:
        clear_tables(conn)
        populate_cinemas(conn)
        populate_movies(conn)
        populate_screenings(conn)
        conn.close()
        print("\nБаза даних успішно заповнена тестовими даними!")
    else:
        print("Не вдалося підключитися до бази даних")

if __name__ == "__main__":
    main()