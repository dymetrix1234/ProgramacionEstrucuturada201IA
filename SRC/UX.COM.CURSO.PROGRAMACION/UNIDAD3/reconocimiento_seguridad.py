print("--- ESCÁNER BIOMÉTRICO DE IA ---")

patron_maestro = [1, 0, 1, 1, 0]
lectura_sensor = []

for i in range(1, 6):
    bit = int(input(f"Ingrese bit {i}: "))
    lectura_sensor.append(bit)

print("\n> Comparando lectura con base de datos...")

coincidencias = 0
for i in range(5):
    if patron_maestro[i] == lectura_sensor[i]:
        coincidencias += 1

porcentaje = (coincidencias / 5) * 100

print(f"> Coincidencias encontradas: {coincidencias}")
print(f"> Porcentaje de Similitud: {porcentaje}%")

if porcentaje == 100:
    estado = "ACCESO TOTAL: Identidad Verificada."
elif 60 <= porcentaje < 100:
    estado = "ADVERTENCIA: Similitud parcial. Se requiere verificación manual."
else:
    estado = "ALERTA: Intruso detectado. Sistema bloqueado."

print(f"ESTADO: {estado}")

print(f"\nPatrón Maestro: {patron_maestro}")
print(f"Lectura Sensor: {lectura_sensor}")