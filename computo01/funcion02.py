print("_______________________________")
print("Jennifer Baires")
print("Código: USTR012824")
print("_______________________________")
print()
# crear la función
def verificar_numero(num):
    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es cero"

# solicitar número
num = int(input("Introduce un número: "))

# imprimir el resultado
print(verificar_numero(num))