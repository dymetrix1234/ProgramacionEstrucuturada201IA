UMBRAL_ALTO = 80.0
UMBRAL_MINIMO = 40.0

instruccion = input("Instrucción recibida: ")
confianza_str = input("Nivel de confianza calculado (%): ")
confianza = float(confianza_str)

if confianza >= UMBRAL_ALTO:
    print(f"Ejecutando la acción: [{instruccion}]... (Éxito)")

elif confianza >= UMBRAL_MINIMO:
    print(f"Confianza insuficiente. ¿Se refiere a: [{instruccion}]? Por favor confirme.")

elif confianza < UMBRAL_MINIMO:
    print(f"Error 404: No pude entender la instrucción. Intente hablar más claro.")

else:
    confianza > 95.0
    print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

print("Sesión de procesamiento finalizada.")