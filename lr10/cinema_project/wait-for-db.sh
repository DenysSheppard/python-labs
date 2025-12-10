import time
import psycopg2
import os

def wait_for_postgres():
    """Очікування готовності PostgreSQL"""
    print("Очікування PostgreSQL...")
    for i in range(30):  # 30 спроб по 2 секунди = 60 секунд
        try:
            conn = psycopg2.connect(
                host=os.getenv('DATABASE_HOST', 'db'),
                port=os.getenv('DATABASE_PORT', '5432'),
                database=os.getenv('DATABASE_NAME', 'cinema_db'),
                user=os.getenv('DATABASE_USER', 'cinema_admin'),
                password=os.getenv('DATABASE_PASSWORD', 'cinema_password')
            )
            conn.close()
            print("PostgreSQL готовий!")
            return True
        except psycopg2.OperationalError as e:
            print(f"Спроба {i+1}/30: {e}")
            time.sleep(2)
    
    print("Не вдалося підключитися до PostgreSQL!")
    return False

if __name__ == "__main__":
    wait_for_postgres()