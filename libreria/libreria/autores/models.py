from django.db import models



# Modelo de Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    imagen= models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre


