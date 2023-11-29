# mi_app/models.py
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_inicio_mandato = models.DateField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_inicio_cursos = models.DateField()
