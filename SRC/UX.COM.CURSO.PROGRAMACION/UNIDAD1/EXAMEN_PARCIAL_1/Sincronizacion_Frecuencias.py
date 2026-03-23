def verificar_sincronizacion():
    """
    Verifica si dos agentes de IA están sincronizados comparando sus frecuencias.
    Dos unidades están sincronizadas si la frecuencia de una es divisor exacto de la otra.
    """
    
    print("=== Sistema de Sincronización de Frecuencias ===\n")
    
    # Solicitar frecuencias
    try:
        freq_a = int(input("Ingrese la frecuencia del Agente A (Hz): "))
        freq_b = int(input("Ingrese la frecuencia del Agente B (Hz): "))
        
        # Validar frecuencias positivas
        if freq_a <= 0 or freq_b <= 0:
            print("\nError: Las frecuencias deben ser valores positivos.")
            return
        
        # Verificar sincronización
        if freq_a == freq_b:
            print(f"\n✓ Sincronización PERFECTA: Ambas frecuencias son iguales ({freq_a} Hz)")
            print("Relación de Sincronización: 1:1")
        
        elif freq_a % freq_b == 0:
            razon = freq_a // freq_b
            print(f"\n✓ Sincronización ESTABLECIDA: {freq_a} Hz es múltiplo de {freq_b} Hz")
            print(f"Relación de Sincronización: {razon}:1 (Agente A)")
        
        elif freq_b % freq_a == 0:
            razon = freq_b // freq_a
            print(f"\n✓ Sincronización ESTABLECIDA: {freq_b} Hz es múltiplo de {freq_a} Hz")
            print(f"Relación de Sincronización: 1:{razon} (Agente B)")
        
        else:
            print(f"\n✗ NO hay Sincronización: {freq_a} Hz y {freq_b} Hz son incompatibles")
            print("No existe relación de divisor exacto entre las frecuencias.")
    
    except ValueError:
        print("\nError: Ingrese valores numéricos enteros válidos.")

# Ejecutar el programa
if __name__ == "__main__":
    verificar_sincronizacion()