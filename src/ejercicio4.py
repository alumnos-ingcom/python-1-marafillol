################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 4
"""
def suma_lenta(numero, otro_numero):
    """Esta función hace que de la suma entre dos números enteros, el segundo se sume de a 1.
    """
    contador = 0
    print(numero,end='')
    limite = abs(otro_numero)
    while contador < limite:
        if otro_numero> 0:
            numero = numero + 1
            print(' + 1',end='')
        else:
            numero = numero - 1
            print(' - 1',end='')
        contador = contador + 1
    resultado = (f" = {numero}")
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = int(input('Ingrese el primer valor: '))
    otro_numero = int(input('Ingrese el segundo valor: '))
    respuesta = suma_lenta(numero, otro_numero)
    print(respuesta)
if __name__ == "__main__":
    principal()
    