from django import forms

from todoum.todoum_admin.models import Movie


class MovieChangeForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieCreationForm(MovieChangeForm):
    pass
