################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 9
"""
def factores_primos(numero):
    """Esta función indica los factores primos del número entero positivo ingresado.
    """
    primo = 2
    lista_de_factores = []
    if numero > 0:
        while primo <= numero:
            while numero % primo == 0:
                lista_de_factores.append(primo)
                numero = numero/primo
            primo = primo + 1
        resultado = tuple(lista_de_factores)
    else:
        resultado = "El número ingresado no es positivo."
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = int(input("Ingrese un numero: "))
    respuesta = factores_primos(numero)
    print(respuesta)
if __name__ == "__main__":
    principal()