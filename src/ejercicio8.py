################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 8
"""
def es_primo(numero):
    """Esta función indica si el número ingresado es primo.
    """
    contador = 0
    divisores = 0
    while contador != numero:
        contador = contador + 1
        if numero % contador == 0:
            divisores = divisores + 1
    respuesta = divisores == 2
    return respuesta
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = int(input('Ingrese un numero: '))
    print(es_primo(numero))
if __name__ == "__main__":
    principal()
    