# Filtrado de Outliers en Sensores de Visión Computacional

def filtrar_y_promediar_lecturas(lecturas):
    """
    Calcula el promedio de lecturas de confianza dentro del rango válido (65%-85%).
    Las lecturas fuera de este rango son consideradas outliers e ignoradas.
    
    Args:
        lecturas (list): Lista de 10 lecturas de confianza del sensor
        
    Returns:
        float: Promedio de lecturas válidas, o None si no hay lecturas válidas
    """
    MINIMO_VALIDO = 65
    MAXIMO_VALIDO = 85
    
    # Filtrar lecturas dentro del rango válido
    lecturas_validas = [
        lectura for lectura in lecturas 
        if MINIMO_VALIDO <= lectura <= MAXIMO_VALIDO
    ]
    
    # Calcular promedio
    if lecturas_validas:
        promedio = sum(lecturas_validas) / len(lecturas_validas)
        return promedio
    else:
        return None


# Ejemplo de uso
if __name__ == "__main__":
    # 10 lecturas del sensor de profundidad (en porcentaje)
    lecturas_sensor = [62, 70, 85, 90, 75, 68, 88, 72, 65, 80]
    
    resultado = filtrar_y_promediar_lecturas(lecturas_sensor)
    
    if resultado is not None:
        print(f"Lecturas del sensor: {lecturas_sensor}")
        print(f"Promedio de lecturas válidas: {resultado:.2f}%")
    else:
        print("No hay lecturas válidas en el rango especificado.")