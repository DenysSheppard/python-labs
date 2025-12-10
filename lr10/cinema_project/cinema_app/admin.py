from django.contrib import admin
from .models import Movie, Cinema, Screening

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'duration', 'rating', 'created_at')
    list_filter = ('genre', 'rating')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ticket_price', 'seats_count', 'address', 'phone')
    search_fields = ('name', 'address')
    list_filter = ('ticket_price',)

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema', 'start_date', 'show_days', 'created_at')
    list_filter = ('start_date', 'cinema')
    search_fields = ('movie__title', 'cinema__name')
    ordering = ('-start_date',)
    raw_id_fields = ('movie', 'cinema')