# Mini Calculadora

print("=== Mini Calculadora ===")
print("Opciones disponibles:")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")

operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división): ")

# Ahora pedimos los números después de elegir la operación
x = float(input("Ingrese num1: "))
y = float(input("Ingrese num2: "))

if operacion == "suma":
    print("Resultado:", x + y)
elif operacion == "resta":
    print("Resultado:", x - y)
elif operacion == "multiplicación":
    print("Resultado:", x * y)
elif operacion == "división":
    if y != 0:
        print("Resultado:", x / y)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("No existe esa operación en mi código")