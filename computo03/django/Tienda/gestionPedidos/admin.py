from django.contrib import admin

from gestionPedidos.models import clientes, articulos, pedidos, proveedores

# Register your models here.
admin.site.register(clientes)
admin.site.register(articulos)
admin.site.register(pedidos)
admin.site.register(proveedores)