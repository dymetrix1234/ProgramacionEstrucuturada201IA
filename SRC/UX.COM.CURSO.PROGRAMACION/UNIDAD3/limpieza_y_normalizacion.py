# --- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---
print("--- SISTEMA DE FILTRADO DE DATOS (SENSOR GPU) ---")

temperaturas = []
contador_errores = 0
numero_lecturas = 8

# Captura de Datos (Arreglo 1D)
for i in range(numero_lecturas):
    lectura = float(input(f"Lectura {i + 1}: "))
    temperaturas.append(lectura)

# Detección de Valores Atípicos (Outliers) y Limpieza
for i in range(numero_lecturas):
    if temperaturas[i] < 0 or temperaturas[i] > 100:
        temperaturas[i] = 35.0
        contador_errores += 1

# Cálculo de la Media Operativa (Sin usar sum() ni len())
suma_total = 0
for temp in temperaturas:
    suma_total += temp

promedio = suma_total / numero_lecturas

# Escritura de Resultados
print(f"\nSe detectaron {contador_errores} lecturas erróneas y fueron corregidas a 35.0.")
print(f"Datos limpios: {temperaturas}")
print(f"Promedio de operación: {promedio:.2f}°C")

# Regla de IA para el sistema de enfriamiento
if promedio > 75:
    print("ALERTA: Activando sistema de enfriamiento líquido")
else:
    print("Estado: Operación normal")