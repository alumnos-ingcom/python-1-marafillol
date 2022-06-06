################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 11
"""
def es_multiplo(numero, multiplo):
    """Esta función indica si un número entero es multiplo de otro, utilizando sumas y restas.
    """
    suma = 0
    if numero > 0 and multiplo > 0:
        while suma < multiplo:
            suma = suma + numero
        resultado = suma == multiplo
    else:
        resultado = "No ha ingresado un número entero positivo"
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = int(input('Ingrese un número: '))
    multiplo = int(input('Ingrese un número: '))
    respuesta = es_multiplo(numero, multiplo)
    print(respuesta)
if __name__ == "__main__":
    principal()
    