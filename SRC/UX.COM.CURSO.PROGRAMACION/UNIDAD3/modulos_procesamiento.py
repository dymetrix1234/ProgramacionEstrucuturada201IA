import math
from datetime import datetime

# --- Módulo de Visualización (Procedimiento) ---
def imprimir_encabezado():
    """Muestra el diseño visual del sistema y la fecha actual."""
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    print("=" * 40)
    print("      SISTEMA DE SALUD INTELIGENTE      ")
    print(f"         Fecha: {fecha_actual}")
    print("=" * 40)

# --- Módulo de Cálculo de IMC (Función) ---
def calcular_imc(peso, estatura):
    """Calcula y retorna el Índice de Masa Corporal."""
    return peso / (estatura ** 2)

# --- Módulo de Análisis de Presión (Función) ---
def evaluar_presion(presion_sistolica):
    """Determina si la presión es Alta o Normal."""
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

# --- Lógica Principal del Programa ---
def ejecutar_diagnostico():
    # 1. Encabezado
    imprimir_encabezado()
    
    # 2. Captura de datos
    nombre = input("Nombre del Paciente: ")
    try:
        peso = float(input("Peso (kg): "))
        estatura = float(input("Estatura (m): "))
        presion = int(input("Presión Sistólica: "))
        
        # 3. Procesamiento de datos (Llamada a funciones)
        resultado_imc = calcular_imc(peso, estatura)
        estado_presion = evaluar_presion(presion)
        
        # 4. Salida de Resultados
        # Se usa math.ceil para redondear el IMC hacia arriba como se solicitó
        imc_redondeado = math.ceil(resultado_imc)
        
        print("\n--- RESULTADOS DEL ANÁLISIS ---")
        print(f"Paciente: {nombre}")
        print(f"IMC Calculado: {imc_redondeado}")
        print(f"Estado de Presión: {estado_presion}")
        print("-" * 31)

    except ValueError:
        print("\n[ERROR] Por favor, ingrese valores numéricos válidos para peso, estatura y presión.")

if __name__ == "__main__":
    ejecutar_diagnostico()