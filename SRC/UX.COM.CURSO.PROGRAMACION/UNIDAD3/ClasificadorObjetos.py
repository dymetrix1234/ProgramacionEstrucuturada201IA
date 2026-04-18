# Definición de constantes
UMBRAL_PEQUENO = 5.0
UMBRAL_GRANDE = 20.0

# Entrada de datos
dimension = float(input("Ingrese el tamaño del objeto detectado (cm): "))

# Lógica de Clasificación
if dimension <= 0.0:
    print("Error: Lectura inválida. Verifique el sensor.")
elif dimension > 0.0 and dimension <= UMBRAL_PEQUENO:
    print("Clasificación: Micro-componente (Grado A)")
elif dimension > UMBRAL_PEQUENO and dimension <= UMBRAL_GRANDE:
    print("Clasificación: Componente Estándar (Grado B)")
else:
    print("Clasificación: Componente Industrial (Grado C)")
    # Operación aritmética adicional
    volumen = dimension ** 3
    print(f"Espacio requerido en contenedor: {volumen} cm3")

# Salida Final
print("Registro de inspección completado.")