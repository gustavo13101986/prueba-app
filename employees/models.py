"""Employees models."""

# Django
from django.contrib.auth.models import User
from django.db import models


class Employees(models.Model):
    """Profile employee."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_name_1 = models.CharField(max_length=100, blank= True)
    last_name_2 = models.CharField(max_length=100, blank= True)
    cedula = models.IntegerField(blank=True)
    birthdate = models.DateField(blank=True)
    genero = models.CharField(max_length=100, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    employee_number = models.IntegerField(blank=True)
    employee_title = models.CharField(max_length=50, blank= True)
    number_jefe = models.IntegerField(blank=True)
    zona = models.CharField(max_length=10, blank= True)
    municipio = models.CharField(max_length=50, blank= True)
    departamento = models.CharField(max_length=50, blank= True)
    ventas_2019 = models.IntegerField(blank=True)
    picture = models.ImageField(
        'Imagen de Perfil',
        upload_to='pictures/', 
        max_length = 200,
        blank=True,
        null=True
    )
    phone_number = models.CharField(max_length=20, blank=True)


    
    def __str__(self):
        """Return username"""
        return self.user.username