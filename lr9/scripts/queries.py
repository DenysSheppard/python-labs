import psycopg2
from tabulate import tabulate
from create_db import create_connection

def print_table(conn, table_name):
    """Виведення таблиці у форматованому вигляді"""
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        
        # Отримуємо назви стовпців
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}' ORDER BY ordinal_position")
        columns = [col[0] for col in cur.fetchall()]
        
        print(f"\n{'='*80}")
        print(f"ТАБЛИЦЯ: {table_name.upper()}")
        print('='*80)
        print(tabulate(rows, headers=columns, tablefmt='grid', floatfmt=".2f"))
        print(f"Всього записів: {len(rows)}")
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виведенні таблиці {table_name}: {e}")

def query_1(conn):
    """Всі комедії, відсортовані по рейтингу"""
    try:
        cur = conn.cursor()
        query = """
        SELECT movie_id, title, genre, duration, rating
        FROM movies
        WHERE genre = 'комедія'
        ORDER BY rating DESC
        """
        cur.execute(query)
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print("ЗАПИТ 1: Всі комедії, відсортовані по рейтингу")
        print('='*80)
        print(tabulate(rows, headers=['ID', 'Назва', 'Жанр', 'Тривалість', 'Рейтинг'], tablefmt='grid', floatfmt=".1f"))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 1: {e}")

def query_2(conn):
    """Остання дата показу фільму для кожного транслювання"""
    try:
        cur = conn.cursor()
        query = """
        SELECT 
            m.title AS Назва_фільму,
            c.name AS Кінотеатр,
            s.start_date AS Початок_показу,
            s.show_days AS Термін_показу,
            s.start_date + s.show_days AS Кінець_показу
        FROM screenings s
        JOIN movies m ON s.movie_id = m.movie_id
        JOIN cinemas c ON s.cinema_id = c.cinema_id
        ORDER BY Кінець_показу DESC
        """
        cur.execute(query)
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print("ЗАПИТ 2: Остання дата показу фільму для кожного транслювання")
        print('='*80)
        print(tabulate(rows, headers=['Назва фільму', 'Кінотеатр', 'Початок показу', 'Термін (днів)', 'Кінець показу'], tablefmt='grid'))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 2: {e}")

def query_3(conn):
    """Максимальний прибуток для кожного кінотеатру від одного показу"""
    try:
        cur = conn.cursor()
        query = """
        SELECT 
            c.name AS Кінотеатр,
            c.ticket_price AS Ціна_квитка,
            c.seats_count AS Кількість_місць,
            ROUND(c.ticket_price * c.seats_count, 2) AS Максимальний_прибуток
        FROM cinemas c
        ORDER BY Максимальний_прибуток DESC
        """
        cur.execute(query)
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print("ЗАПИТ 3: Максимальний прибуток для кожного кінотеатру від одного показу")
        print('='*80)
        print(tabulate(rows, headers=['Кінотеатр', 'Ціна квитка', 'Кількість місць', 'Максимальний прибуток'], tablefmt='grid', floatfmt=".2f"))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 3: {e}")

def query_4(conn, genre):
    """Всі фільми заданого жанру"""
    try:
        cur = conn.cursor()
        query = """
        SELECT movie_id, title, genre, duration, rating
        FROM movies
        WHERE genre = %s
        ORDER BY title
        """
        cur.execute(query, (genre,))
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print(f"ЗАПИТ 4: Всі фільми жанру '{genre}'")
        print('='*80)
        print(tabulate(rows, headers=['ID', 'Назва', 'Жанр', 'Тривалість', 'Рейтинг'], tablefmt='grid', floatfmt=".1f"))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 4: {e}")

def query_5(conn):
    """Кількість фільмів кожного жанру"""
    try:
        cur = conn.cursor()
        query = """
        SELECT 
            genre AS Жанр,
            COUNT(*) AS Кількість_фільмів,
            AVG(rating) AS Середній_рейтинг,
            AVG(duration) AS Середня_тривалість
        FROM movies
        GROUP BY genre
        ORDER BY Кількість_фільмів DESC
        """
        cur.execute(query)
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print("ЗАПИТ 5: Кількість фільмів кожного жанру")
        print('='*80)
        print(tabulate(rows, headers=['Жанр', 'Кількість фільмів', 'Середній рейтинг', 'Середня тривалість'], tablefmt='grid', floatfmt=".1f"))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 5: {e}")

def query_6(conn):
    """Кількість фільмів кожного жанру в кожному кінотеатрі (перехресний запит)"""
    try:
        cur = conn.cursor()
        query = """
        сді
        """
        cur.execute(query)
        rows = cur.fetchall()
        
        print(f"\n{'='*80}")
        print("ЗАПИТ 6: Кількість фільмів кожного жанру в кожному кінотеатрі")
        print('='*80)
        print(tabulate(rows, headers=['Кінотеатр', 'Мелодрами', 'Комедії', 'Бойовики', 'Всього фільмів'], tablefmt='grid'))
        
        cur.close()
    except Exception as e:
        print(f"Помилка при виконанні запиту 6: {e}")

def main():
    conn = create_connection()
    if conn is not None:
        print("\n" + "="*80)
        print("ЛАБОРАТОРНА РОБОТА №9: СИСТЕМА УПРАВЛІННЯ КІНОТЕАТРАМИ")
        print("="*80)
        
        # Виведення всіх таблиць
        print("\n" + "="*80)
        print("ВСІ ТАБЛИЦІ БАЗИ ДАНИХ:")
        print("="*80)
        
        print_table(conn, "movies")
        print_table(conn, "cinemas")
        print_table(conn, "screenings")
        
        # Виконання запитів
        print("\n" + "="*80)
        print("РЕЗУЛЬТАТИ ВИКОНАННЯ ЗАПИТІВ:")
        print("="*80)
        
        query_1(conn)  # Всі комедії, відсортовані по рейтингу
        query_2(conn)  # Остання дата показу
        query_3(conn)  # Максимальний прибуток
        query_4(conn, "мелодрама")  # Фільми заданого жанру
        query_5(conn)  # Кількість фільмів кожного жанру
        query_6(conn)  # Перехресний запит
        
        conn.close()
    else:
        print("Не вдалося підключитися до бази даних")

if __name__ == "__main__":
    main()