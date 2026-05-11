print("--- TELEMETRÍA DE CLUSTER IA ---")

temp = float(input("Temperatura actual (°C): "))
vram = int(input("Uso de Memoria VRAM (%): "))
cooling = input("¿Enfriamiento activo? (si/no): ").lower()

if vram < 0 or vram > 100:
    print("Error: Lectura de memoria fuera de rango (0-100%).")
else:
    if temp > 90 or vram == 100:
        print("¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")
    elif 75 <= temp <= 90:
        if cooling == "no":
            print("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
        elif cooling == "si":
            print("Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
    elif temp < 75 and vram < 80:
        print("Sistema Estable: Entrenamiento en curso a máxima capacidad.")
        free = 100 - vram
        print(f"Memoria VRAM libre: {free}%")