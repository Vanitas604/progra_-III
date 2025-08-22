#crear la funcion
def cuadrado_numero(num1):
    return num1 ** 2

#solicita la variable
num1 = int(input("Introduce el número para calcular: "))

#imprimir el resultado
print(f"El cuadrado de {num1} es {cuadrado_numero(num1)}")