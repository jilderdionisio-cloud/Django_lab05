from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "duration_minutes", "release_date", "is_active")
    list_filter = ("is_active", "release_date")
    search_fields = ("title",)