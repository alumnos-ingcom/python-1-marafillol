################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def compara(numero, otro_numero):
    """Esta función determina si el primer número es mayor, menor o igual al segundo.
    """
    suma_1 = numero + numero
    suma_2 = otro_numero + otro_numero
    resta_1 = numero - otro_numero
    resta_2 = otro_numero - otro_numero
    if suma_1 < suma_2:
        resultado = -1
    elif resta_1 == resta_2:
        resultado = 0
    else:
        resultado = 1
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    numero = float(input("Ingrese un numero:  "))
    otro_numero = float(input("Ingrese un numero:  "))
    print(compara(numero, otro_numero))
if __name__ == "__main__":
    principal()
