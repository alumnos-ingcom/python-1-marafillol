################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 5
"""
def division_lenta(dividendo, divisor):
    """Esta función obtiene el cociente y resto de dos números enteros, mediante restas sucesivas.
    """
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    resto = dividendo
    resultado = (cociente, resto)
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    dividendo = int(input("Ingrese un numero: "))
    divisor = int(input("Ingrese un numero: "))
    respuesta = division_lenta(dividendo, divisor)
    print(f"El cociente es {respuesta[0]} y el resto es {respuesta[1]}.")
if __name__ == "__main__":
    principal()
