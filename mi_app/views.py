# mi_app/views.py
from django.shortcuts import render, redirect
from .forms import ProfesorForm, DirectorForm, AlumnoForm, BuscarForm
from .models import Profesor, Director, Alumno

def profesor_form(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_form')
    else:
        form = ProfesorForm()

    return render(request, 'mi_app/profesor_form.html', {'form': form})

def director_form(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_form')
    else:
        form = DirectorForm()

    return render(request, 'mi_app/director_form.html', {'form': form})

def alumno_form(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_form')
    else:
        form = AlumnoForm()

    return render(request, 'mi_app/alumno_form.html', {'form': form})

def buscar(request):
    if 'query' in request.GET:
        query = request.GET['query']
        # Realiza la búsqueda en los modelos de Profesor, Director y Alumno
        resultados_profesor = Profesor.objects.filter(nombre__icontains=query)
        resultados_director = Director.objects.filter(nombre__icontains=query)
        resultados_alumno = Alumno.objects.filter(nombre__icontains=query)

        return render(request, 'mi_app/buscar.html', {
            'query': query,
            'resultados_profesor': resultados_profesor,
            'resultados_director': resultados_director,
            'resultados_alumno': resultados_alumno,
        })
    else:
        return render(request, 'mi_app/buscar.html')

def home(request):
    return render(request, 'mi_app/home.html')
