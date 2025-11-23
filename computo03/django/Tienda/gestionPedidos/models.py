from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

class articulos(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()

class pedidos(models.Model):
    N_Pedido=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()