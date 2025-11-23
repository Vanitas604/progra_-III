from django.http import HttpResponse
from django.template import Context, Template
 
def helloword(resquest):
    return HttpResponse("Hola mundo, desde Django")

def miPrimerPlantilla(request):
    plantillaExterna = open("C:/Users/jenni/Desktop/Progra III Visual Code/progra_-III/computo03/django/plantilla/plantilla/Miplantilla.html")
    plantilla01 = Template(plantillaExterna.read())
    plantillaExterna.close()
    Contexto= Context()
    pagina01=plantilla01.render(Contexto)
    return HttpResponse(pagina01)

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >=60:
            categoria="Tercera edad"
        else:
            categoria="Adultez"
        
    else:
        if edad<10:
            categoria="Infancia"
        
        else:
            categoria="Adolescencia"
        
    resultado=""" <h1>Categoria de la edad: %s"""%categoria
    return HttpResponse(resultado)

def miPrimeraPlantilla02(request):
    nombre= "Jennifer Baires"
    plantillaExterna = open("C:/Users/jenni/Desktop/Progra III Visual Code/progra_-III/computo03/django/plantilla/plantilla/parametro.html")
    plantilla02 = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto= Context({"nombreUser": nombre})
    documento01=plantilla02.render(contexto)
    return HttpResponse(documento01)

