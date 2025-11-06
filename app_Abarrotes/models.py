from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    # Campo para la foto del empleado
    foto = models.ImageField(upload_to='empleados/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"