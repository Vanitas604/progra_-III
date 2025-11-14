"""
URL configuration for prograIII project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prograIII.views import saludo  # Importar la vista saludo
from prograIII.views import despedida  # Importar la vista despedida
from prograIII.views import calcularedad  # Importar la vista calcularedad
from prograIII.views import operaciones  # Importar la vista operaciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', saludo),  # Nueva ruta para la vista saludo
    path('goodbye/', despedida),  # Nueva ruta para la vista despedida
    path('edad/<int:agno>/', calcularedad),  # Nueva ruta para la vista calcularedad
    path('operaciones/<int:num1>/<int:num2>/', operaciones),  # Nueva ruta para operaciones
]
