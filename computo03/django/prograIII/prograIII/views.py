from django.http import HttpResponse

def saludo(request): #esta es mi primer vista
    pagina = """
    <html>
    <body>
    <h2>
    Hola Mundo, esta es mi primera vista en Django!
    </h2>
    </body>
    </html>"""
    return HttpResponse(pagina)

def despedida(request): #esta es mi primer vista
    pagina = """
    <html>
    <body>
    <h2>
    Fue un gusto trabajar con ustedes!
    </h2>
    </body>
    </html>"""
    return HttpResponse(pagina)

def calcularedad(request, agno):
    edadactual = 19
    agnoactual = 2025
    tiempo = agno - agnoactual
    edadfutura = edadactual + tiempo
    pagina = """
    <html>
    <body>
    <h2>
    En el año %s tendrás %s
    </h2>
    </body>
    </html>""" % (agno, edadfutura)
    return HttpResponse(pagina)

def operaciones(request, num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = round(num1 / num2, 2) if num2 != 0 else "No se puede dividir entre 0"

def operaciones(request, num1, num2):

    # Cálculos matemáticos básicos
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    # Evita división entre cero
    division = round(num1 / num2, 2) if num2 != 0 else "No se puede dividir entre 0"

    # Retorno del HTML con tu mismo diseño original (solo cambiados los colores)
    return HttpResponse(f"""
        <html>
            <body 
                style="
                    background-color:#e3f2fd;   /* Fondo azul claro */
                    text-align:center; 
                    padding-top:50px; 
                    font-family:Arial;
                "
            >
            
                <!-- Título principal -->
                <h2 style="color:#0d47a1;">Operaciones Básicas</h2>
                
                <!-- Números ingresados -->
                <p><strong style="color:#1e88e5;">Primer número:</strong> {num1}</p>
                <p><strong style="color:#1e88e5;">Segundo número:</strong> {num2}</p>

                <!-- Línea divisoria -->
                <hr style="width:50%; border:1px solid #90caf9;">

                <!-- Resultados de operaciones -->
                <p><strong style="color:#1565c0;">Suma:</strong> {suma}</p>
                <p><strong style="color:#1565c0;">Resta:</strong> {resta}</p>
                <p><strong style="color:#1565c0;">Multiplicación:</strong> {multiplicacion}</p>
                <p><strong style="color:#1565c0;">División:</strong> {division}</p>

            </body>
        </html>
    """)
