################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 11
"""
def es_multiplo(numero, multiplo):
    """Esta función que indica si un número entero es multiplo de otro, utilizando sumas y restas.
    """
    if numero > 0 and multiplo > 0:
        while numero < multiplo:
            numero = numero + numero
        resultado = numero == multiplo
    else:
        resultado = "Ingrese un número entero positivo"
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = int(input('Ingrese un numero: '))
    multiplo = int(input('Ingrese un multiplo: '))
    print(es_multiplo(numero, multiplo))
if __name__ == "__main__":
    principal()
    