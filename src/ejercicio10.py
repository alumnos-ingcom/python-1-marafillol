################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""EJERCICIO 10
"""
def es_palindromo(texto):
    """Esta función identifica si un texto es palindromo"""
    lista = list(texto)
    limite = len(texto)
    contador = 0
    nuevo = ""
    while contador != limite:
        nuevo = nuevo + lista.pop()
        contador = contador+1
    resultado = nuevo == texto
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    texto = input("Ingrese una palabra: ")
    print(es_palindromo(texto))
if __name__ == "__main__":
    principal()
    