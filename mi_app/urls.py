# mi_app/urls.py
from django.urls import path
from .views import profesor_form, director_form, alumno_form, buscar, home

urlpatterns = [
    path('profesor/', profesor_form, name='profesor_form'),
    path('director/', director_form, name='director_form'),
    path('alumno/', alumno_form, name='alumno_form'),
    path('buscar/', buscar, name='buscar'),
    path('', home, name='home'),
]
