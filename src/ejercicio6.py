################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 6
"""
def ordenar_mayor_a_menor(uno, dos, tres):
    """ Esta función ordena de mayor a menor los 3 valores ingresados.
    """
    if uno >= dos >= tres:
        resultado = (uno, dos, tres)
    elif uno >= tres >= dos:
        resultado = (uno, tres, dos)
    elif dos >= uno >= tres:
        resultado = (dos, uno, tres)
    elif dos >= tres >= uno:
        resultado = (dos, tres, uno)
    elif tres >= uno >= dos:
        resultado = (tres, uno, dos)
    elif tres >= dos >= uno:
        resultado = (tres, dos, uno)
    return resultado
def ordenar_menor_a_mayor(uno, dos, tres):
    """ Esta función ordena de menor a mayor los 3 valores ingresados.
    """
    if uno <= dos <= tres:
        resultado = (uno, dos, tres)
    elif uno <= tres <= dos:
        resultado = (uno, tres, dos)
        print(resultado)
    elif dos <= uno <= tres:
        resultado = (dos, uno, tres)
    elif dos <= tres <= uno:
        resultado = (dos, tres, uno)
    elif tres <= uno <= dos:
        resultado = (tres, uno, dos)
    elif tres <= dos <= uno:
        resultado = (tres, dos, uno)
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    uno = int(input("Ingrese un numero: "))
    dos = int(input("Ingrese un numero: "))
    tres = int(input("Ingrese un numero: "))
    respuesta1 = ordenar_mayor_a_menor(uno, dos, tres)
    respuesta2 = ordenar_menor_a_mayor(uno, dos, tres)
    print(respuesta1)
    print(respuesta2)
if __name__ == "__main__":
    principal()
    