# FiltroSeguridadIA.py

# Declaracion de constantes
LIMITE_SUPERIOR = 100.0
LIMITE_INFERIOR = 0.0

# Entrada de datos
lectura_input = input("Ingrese la lectura del sensor térmico: ")
lectura = float(lectura_input)

# Validacion y Procesamiento (Logica de IA)
if lectura >= LIMITE_INFERIOR and lectura <= LIMITE_SUPERIOR:
    # Normalizacion
    dato_normalizado = lectura / LIMITE_SUPERIOR
    print("Señal aceptada. Valor normalizado para el modelo:", dato_normalizado)
else:
    # Bloque de datos no validos
    print("Error: Lectura fuera de rango. La señal se considera ruido.")

# Salida Final
print("Fin del proceso de filtrado de datos.")