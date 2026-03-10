'''
definir una función que tome un puntaje numérico y devuelva la calificación correspondiente según la siguiente escala:
'''
def calificacion (puntaje):
    if puntaje < 0 or puntaje > 100:
        return "Puntaje inválido. Debe estar entre 0 y 100."
    if puntaje >= 90:
        return "A"
    elif puntaje >= 80:
        return "B"
    elif puntaje >= 70:
        return "C"
    elif puntaje >= 60:
        return "D"
    else:
        return "F"
# Solicitar al usuario que ingrese el puntaje
puntaje_usuario = float(input("Ingrese el puntaje del estudiante: "))
# Obtener la calificación correspondiente
calificacion_usuario = calificacion(puntaje_usuario)
# Mostrar la calificación al usuario
print(f"La calificación del estudiante es: {calificacion_usuario}")