from django.contrib import admin

from todoum.todoum_admin.forms import MovieChangeForm, MovieCreationForm
from todoum.todoum_admin.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieChangeForm
    add_form = MovieCreationForm
    list_display = ("name",)
