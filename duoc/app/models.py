from django.db import models
from django.urls import reverse

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    rut = models.CharField(max_length=200, null=False)
    direccion = models.CharField(max_length=200, null=True)
    carrera = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre
    
    # The absolute path to get the url then reverse into 'estudiante_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('estudiante_edit', kwargs={'pk': self.pk})
