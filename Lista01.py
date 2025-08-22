print("________________________________________________")
print("Lista - sumar todos")
print("________________________________________________")
#solicitar un número final de la lista
num1=int(input("Ingrese un numero hasta el 100: "))

#crear lista desde 1 hasta el $num1
lista = list(range(1, num1+1))

#Calcular la suma5
resultado=sum(lista)

#Imprimir el resultado
print(f"La suma de la lista hasta {num1} es {resultado}")
