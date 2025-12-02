from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(blank=True, null=True, max_length=15)

class articulos(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class pedidos(models.Model):
    N_Pedido=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

class proveedores(models.Model):
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    seccion=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=15)
