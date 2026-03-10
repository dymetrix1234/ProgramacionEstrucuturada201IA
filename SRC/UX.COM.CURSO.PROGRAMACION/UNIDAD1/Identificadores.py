
def imprimir_identificadores():
    # Identificadores validos
    nombre_usuario ="Alumno" #inicia co letra y tiene _
    sensor = "temperatura" # inicia con letra
    _id_interno = 12 #puede contener _ y numeros

    print(nombre_usuario)
    print(sensor)
    print(_id_interno)

# nombre correcto de funciones
def calcular_area():
    print("calculanndo area...")

def main():
    imprimir_identificadores()
    calcular_area()

if __name__ == "__main__":
    main()
