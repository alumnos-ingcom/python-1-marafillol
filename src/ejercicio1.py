################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def convertir_a_fahrenheit(centigrados):
    """Esta función convierte grados centigrados a grados fahrenheit.
    """
    fahrenheit = (1.8 * centigrados) + 32
    resultado = (f'{centigrados}° grados centigrados son {fahrenheit}° grados fahrenheit')
    return resultado
def convertir_a_centigrados(fahrenheit):
    """Esta función convierte grados fahrenheit a grados centigrados.
    """
    centigrados = (fahrenheit - 32) * 5/9
    resultado = (f'{fahrenheit}° grados fahrenheit son {centigrados}° grados centigrados')
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    centigrados = float(input("Ingrese el grado que desea convertir: "))
    fahrenheit = float(input("Ingrese el grado que desea convertir: "))
    print(convertir_a_fahrenheit(centigrados))
    print(convertir_a_centigrados(fahrenheit))
if __name__ == "__main__":
    principal()
