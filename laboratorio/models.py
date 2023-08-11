from django.db import models
from django.core.validators import MinValueValidator
import datetime


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
   
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    especialidad = models.CharField(max_length=255)
   
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.DateField(default=datetime.date(2015, 1, 1),
                                         validators=[MinValueValidator(datetime.date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
   
    def __str__(self):
        return self.nombre