from django.contrib import admin
from kinopoisk.models import *
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'genres',
        'description',
        'release_date',
        'rating',
        'directors',
        'actors',
        'budget',
        'poster',
    )
@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'movie',
        'text',
        'likes',
        'created_at',
    )