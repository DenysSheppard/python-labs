from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('мелодрама', 'Мелодрама'),
        ('комедія', 'Комедія'),
        ('бойовик', 'Бойовик'),
    ]
    
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Назва фільму")
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name="Жанр")
    duration = models.IntegerField(verbose_name="Тривалість (хв)")
    rating = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    class Meta:
        db_table = 'movies'
        verbose_name = 'Фільм'
        verbose_name_plural = 'Фільми'
    
    def __str__(self):
        return self.title

class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Назва кінотеатру")
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна квитка")
    seats_count = models.IntegerField(verbose_name="Кількість місць")
    address = models.CharField(max_length=500, verbose_name="Адреса")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    class Meta:
        db_table = 'cinemas'
        verbose_name = 'Кінотеатр'
        verbose_name_plural = 'Кінотеатри'
    
    def __str__(self):
        return self.name

class Screening(models.Model):
    screening_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фільм", db_column='movie_id')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name="Кінотеатр", db_column='cinema_id')
    start_date = models.DateField(verbose_name="Дата початку показу")
    show_days = models.IntegerField(verbose_name="Кількість днів показу")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    class Meta:
        db_table = 'screenings'
        verbose_name = 'Показ'
        verbose_name_plural = 'Покази'
    
    def __str__(self):
        return f"{self.movie.title} в {self.cinema.name}"