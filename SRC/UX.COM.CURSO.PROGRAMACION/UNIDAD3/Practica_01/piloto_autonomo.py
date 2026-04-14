# Simulación de un piloto autónomo para un vehículo

# Solicitar datos de sensores al usuario
distancia = float(input("ingresa la distancia al objeto mas cercano en metros: "))
color = input("ingresa el color del semaforo (rojo, verde, amarillo): ").lower()
peaton = input("ingresa si hay peatones cruzando (si/no): ").lower()

# Evaluar condiciones para el piloto autónomo
if distancia < 5:
    print("FRENO DE EMERGENCIA ACTIVADO")
elif peaton == "si":
    print("FRENO DE EMERGENCIA ACTIVADO")
elif color == "rojo":
    print("estado detenido, esperando luz verde")
elif color == "amarillo":
    print("estado precaucion, reduciendo velocidad para detenerse")
elif color == "verde" and distancia >= 5 and peaton == "no":
    print("estado en movimiento, todo despejado para avanzar")
else:
    print("Error en la entrada de sensores, color de semaforo no reconocido o valor de distancia invalido")


# Validación de entradas
if distancia < 0:
    print("Error: La distancia no puede ser negativa")
elif color not in ["rojo", "verde", "amarillo"]:
    print("Error: Color de semáforo no válido. Use 'rojo', 'verde' o 'amarillo'")
elif peaton not in ["si", "no"]:
    print("Error: Ingrese 'si' o 'no' para peatones")
else:
    # Simulación de monitoreo constante de sensores
    pass
print("Monitoreo de sensores constante... Sistema activo.")
