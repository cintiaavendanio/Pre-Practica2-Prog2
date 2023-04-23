# Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
# el resultado de la división entre ambos numeros.

# En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


# INICIO
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

try:
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except:
    print("ocurrio un error")
# FIN