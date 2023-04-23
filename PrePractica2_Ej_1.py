# Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

# Nota : Hacerlo con la función max(a,b) y luego con una comparación

# # OPCION1 INICIO
# numeros = input("Ingrese una lista de números separados por un espacio: ")
# # Convertir la cadena de entrada en una lista de números
# numeros_lista = numeros.split(" ")

# # Encontrar el máximo número en la lista
# maximo_numero = max(numeros_lista)

# # Imprimir el resultado
# print("El máximo número en la lista es:", maximo_numero)

# # FIN

# OPCION 2 INICIO
num1 = int(input("ingrese primer numero"))
num2 = int(input("ingrese segundo numero"))

print("el mayornumero entre ", num1, " y ", num2, " es ", max(num1, num2))

# FIN