from django.db import models
from libreria.autores.models import Autor

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    imagen= models.TextField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo
