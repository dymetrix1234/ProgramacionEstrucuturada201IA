# --- MÓDULO DE SENSORES (VECTORES) ---
print("--- MÓDULO DE SENSORES (VECTORES) ---")
sensores_distancia = []
suma_distancias = 0

for i in range(5):
    distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
    sensores_distancia.append(distancia)
    suma_distancias += distancia

promedio = suma_distancias / 5
print(f"\nPromedio de proximidad: {promedio:.2f}m.")

if promedio < 2.0:
    print("Aviso: Reduciendo velocidad global")
else:
    print("Estado: Seguro.")

print("\n" + "-"*35 + "\n")

# --- MÓDULO DE VISIÓN (MATRICES) ---
print("--- MÓDULO DE VISIÓN (MATRICES) ---")
print("Llenando matriz de cámara 3x3:")

camara_ia = []
for f in range(3):
    fila = []
    for c in range(3):
        brillo = int(input(f"Fila {f}, Col {c} (Brillo 0-255): "))
        
        # Operación de saturación
        if brillo > 255:
            brillo = 255
        elif brillo < 0:
            brillo = 0
            
        fila.append(brillo)
    camara_ia.append(fila)

# Escritura de Arreglo (Formato tabla)
print("\nVisualización de la imagen capturada:")
for fila in camara_ia:
    print(f"[ {'  '.join(f'{pixel:3}' for pixel in fila)} ]")

# --- PARTE 3: ANÁLISIS DE LA MATRIZ ---
puntos_brillantes = 0
for fila in camara_ia:
    for pixel in fila:
        if pixel > 200:
            puntos_brillantes += 1

print("\nResultado de Análisis IA:")
print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")