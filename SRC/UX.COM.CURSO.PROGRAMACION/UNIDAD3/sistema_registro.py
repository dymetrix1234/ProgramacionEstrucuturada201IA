class MonitorEntrenamiento:
    def __init__(self, umbral=0.01):
        self.historial_errores = []
        self.umbral_convergencia = float(umbral)

    def registrar_epoca(self, valor_error):
        # Lógica de registro
        self.historial_errores.append(valor_error)
        
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión ({valor_error}).")
            return True # Retornamos True para saber si terminó por convergencia
        return False

# --- Flujo Principal ---
print("--- Iniciando Monitor de Red Neuronal ---")
monitor = MonitorEntrenamiento(umbral=0.05)
epocas_a_registrar = 5
contador = 1

while contador <= epocas_a_registrar:
    try:
        entrada = input(f"Ingrese el error de la Época {contador}: ")
        valor = float(entrada)
        
        # Validación de números negativos
        if valor < 0:
            print("> [ERROR] El error de entrenamiento no puede ser negativo.")
            continue
            
        convergencia = monitor.registrar_epoca(valor)
        print("> Registro exitoso.")
        
        if convergencia:
            break
            
        contador += 1

    except ValueError:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")

# --- Análisis de Datos Final ---
if monitor.historial_errores:
    print("\n" + "--- Resumen de Entrenamiento ---")
    print(f"Historial: {monitor.historial_errores}")
    
    # Cálculos
    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    mejor_error = min(monitor.historial_errores)
    
    print(f"Promedio de Error: {promedio:.4f}")
    print(f"Mejor resultado obtenido: {mejor_error}")
else:
    print("\nNo se registraron datos válidos para el análisis.")