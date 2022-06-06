################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 2
"""
def signo(numero):
    """Esta función determina si el número ingresado es positivo, neutro o negativo.
    """
    calculo = numero + numero
    if calculo > 0:
        resultado = 1
    elif calculo == 0:
        resultado = 0
    else:
        resultado = -1
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = float(input("Ingrese un numero:  "))
    respuesta = signo(numero)
    print(respuesta)
if __name__ == "__main__":
    principal()
