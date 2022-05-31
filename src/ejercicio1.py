################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def convertir_a_fahrenheit(centigrados):
    """Esta función convierte grados centigrados a grados fahrenheit.
    """
    resultado_fahrenheit = (1.8 * centigrados) + 32
    return resultado_fahrenheit
def convertir_a_centigrados(fahrenheit):
    """Esta función convierte grados fahrenheit a grados centigrados.
    """
    resultado_centigrados = (fahrenheit - 32) * 5/9
    return resultado_centigrados
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    centigrados = float(input("Ingrese los grados centigrados: "))
    fahrenheit = float(input("Ingrese los grados fahrenheit: "))
    respuesta_de_f = convertir_a_fahrenheit(centigrados)
    respuesta_de_c = convertir_a_centigrados(fahrenheit)
    print(f"{centigrados}° centigrados son equivalentes a {respuesta_de_f}° fahrenheit.")
    print(f"{fahrenheit}° fahrenheit son equivalentes a {respuesta_de_c}° centigrados.")
if __name__ == "__main__":
    principal()
