################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def division_lenta(dividiendo, divisor):
    """Esta función obtiene el cociente y resto de dos numeros enteros, mediante restas sucesivas.
    """
    cociente = 0
    while dividiendo >= divisor:
        dividiendo = dividiendo - divisor
        cociente = cociente + 1
    resto = dividiendo
    resultado = cociente, resto
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    dividiendo = int(input("Ingrese un numero: "))
    divisor = int(input("Ingrese un numero: "))
    respuesta = division_lenta(dividiendo, divisor)
    print(f"El cociente es {respuesta[0]} y el resto es {respuesta[1]}.")
if __name__ == "__main__":
    principal()
