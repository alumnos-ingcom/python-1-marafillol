################
# Mara Fillol - @marafillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def sexadecimal_a_decimal(horas, minutos, segundos):
    """Esta función convierte las horas, minutos y segundos ingresados a segundos.
    """
    minutos = minutos+(horas*60)
    segundos = segundos+(minutos*60)
    return segundos
def decimal_a_sexadecimal(numero):
    """Esta función convierte los segundos a horas, minutos y segundos.
    """
    numero_hora = (numero//60)//60
    numero_minuto = (numero//60)%60
    numero_segundo = numero%60
    resultado = (numero_hora, numero_minuto, numero_segundo)
    return resultado
def principal():
    """
    Esta función es la parte interactiva del programa.
    """
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese las minutos: "))
    segundos = int(input("Ingrese las segundos: "))
    numero = sexadecimal_a_decimal(horas, minutos, segundos)
    print(f"En total son {numero} segundos.")
    respuesta_sexadecimal = decimal_a_sexadecimal(numero)
    print(f"{numero} segundos son equivalentes a {respuesta_sexadecimal}.")
if __name__ == "__main__":
    principal()
