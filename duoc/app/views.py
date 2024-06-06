from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Estudiante

# Create your views here.

class EstudianteList(ListView):
    model = Estudiante

class EstudianteDetail(DetailView):
    model = Estudiante

class EstudianteCreate(CreateView):
    model = Estudiante
    # Field must be same as the model attribute
    fields = ['nombre', 'rut', 'direccion', 'carrera']
    success_url = reverse_lazy('estudiante_lista')

class EstudianteUpdate(UpdateView):
    model = Estudiante
    # Field must be same as the model attribute
    fields = ['nombre', 'rut', 'direccion', 'carrera']
    success_url = reverse_lazy('estudiante_lista')

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_lista')