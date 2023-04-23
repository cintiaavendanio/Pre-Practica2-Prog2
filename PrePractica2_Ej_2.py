# Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

# El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

# INICIO
numeros = input("Ingresa una lista de números separados por un espacio: ")

listaDeNumeros = numeros.split(" ")

impares = []

# Iteramos sobre la lista de números ingresados por el usuario
for num in listaDeNumeros:
    if int(num) % 2 != 0:
        impares.append(num)

# Imprimimos la lista de impares
print("Los números es:", listaDeNumeros)
print("Los números impares son:", impares)

# FIN
