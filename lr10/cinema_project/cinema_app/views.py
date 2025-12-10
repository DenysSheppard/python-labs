from django.shortcuts import render
from django.db import connection
from collections import OrderedDict

def index(request):
    student_info = {
        'name': 'Постумент Денис Андрійович',
        'group': 'Група ІПЗ-23008бск',
    }
    
    tables_data = {}
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT movie_id, title, genre, duration, rating, created_at FROM movies ORDER BY movie_id")
        movies = cursor.fetchall()
        tables_data['movies'] = {
            'headers': ['ID', 'Назва', 'Жанр', 'Тривалість', 'Рейтинг', 'Дата створення'],
            'rows': movies
        }
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT cinema_id, name, ticket_price, seats_count, address, phone, created_at FROM cinemas ORDER BY cinema_id")
        cinemas = cursor.fetchall()
        tables_data['cinemas'] = {
            'headers': ['ID', 'Назва', 'Ціна квитка', 'Місць', 'Адреса', 'Телефон', 'Дата створення'],
            'rows': cinemas
        }

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                s.screening_id,
                m.title AS movie_title,
                c.name AS cinema_name,
                s.start_date,
                s.show_days,
                s.created_at
            FROM screenings s
            JOIN movies m ON s.movie_id = m.movie_id
            JOIN cinemas c ON s.cinema_id = c.cinema_id
            ORDER BY s.screening_id
        """)
        screenings = cursor.fetchall()
        tables_data['screenings'] = {
            'headers': ['ID', 'Фільм', 'Кінотеатр', 'Дата початку', 'Дні показу', 'Дата створення'],
            'rows': screenings
        }
    
    context = {
        'student_info': student_info,
        'tables': tables_data,
    }
    
    return render(request, 'cinema_app/index.html', context)