import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    """Створення з'єднання з базою даних"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="cinema_db",
            user="cinema_admin",
            password="cinema_password"
        )
        return conn
    except Exception as e:
        print(f"Помилка підключення до БД: {e}")
        return None

def create_tables(conn):
    """Створення таблиць у базі даних"""
    commands = [
        """
        CREATE TABLE IF NOT EXISTS movies (
            movie_id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            genre VARCHAR(50) CHECK (genre IN ('мелодрама', 'комедія', 'бойовик')),
            duration INTEGER NOT NULL CHECK (duration > 0),
            rating DECIMAL(3,1) CHECK (rating >= 0 AND rating <= 10),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS cinemas (
            cinema_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            ticket_price DECIMAL(6,2) NOT NULL CHECK (ticket_price > 0),
            seats_count INTEGER NOT NULL CHECK (seats_count > 0),
            address VARCHAR(500) NOT NULL,
            phone VARCHAR(20) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS screenings (
            screening_id SERIAL PRIMARY KEY,
            movie_id INTEGER NOT NULL,
            cinema_id INTEGER NOT NULL,
            start_date DATE NOT NULL,
            show_days INTEGER NOT NULL CHECK (show_days > 0),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            FOREIGN KEY (movie_id) 
                REFERENCES movies(movie_id) 
                ON DELETE CASCADE,
            
            FOREIGN KEY (cinema_id) 
                REFERENCES cinemas(cinema_id) 
                ON DELETE CASCADE
        )
        """
    ]
    
    try:
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        conn.commit()
        cur.close()
        print("Таблиці успішно створені!")
    except Exception as e:
        print(f"Помилка при створенні таблиць: {e}")
        conn.rollback()

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
        conn.close()
    else:
        print("Не вдалося підключитися до бази даних")

if __name__ == "__main__":
    main()