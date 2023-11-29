# mi_app/forms.py
from django import forms
from .models import Profesor, Director, Alumno
from django.core.exceptions import ValidationError
from django.utils import timezone

class ProfesorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Profesor
        fields = '__all__'

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del profesor debe tener al menos 3 caracteres.")
        return nombre

class DirectorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    fecha_inicio_mandato = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Director
        fields = '__all__'

    def clean_fecha_inicio_mandato(self):
        fecha_inicio_mandato = self.cleaned_data['fecha_inicio_mandato']
        if fecha_inicio_mandato > timezone.now().date():
            raise ValidationError("La fecha de inicio de mandato no puede ser en el futuro.")
        return fecha_inicio_mandato

class AlumnoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    fecha_inicio_cursos = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Alumno
        fields = '__all__'

    def clean_fecha_inicio_cursos(self):
        fecha_inicio_cursos = self.cleaned_data['fecha_inicio_cursos']
        if fecha_inicio_cursos > timezone.now().date():
            raise ValidationError("La fecha de inicio de cursos no puede ser en el futuro.")
        return fecha_inicio_cursos

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)