################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def signo(numero):
    """Esta función determina si el número ingresado es positivo, neutro o negativo.
    """
    calculo = numero + numero
    if calculo > 0:
        calculo = 'positivo'
    elif calculo == 0:
        calculo = 'neutro'
    else:
        calculo = 'negativo'
    resultado = (f"{numero} es {calculo}")
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = float(input("Ingrese un numero:  "))
    print(signo(numero))
if __name__ == "__main__":
    principal()
