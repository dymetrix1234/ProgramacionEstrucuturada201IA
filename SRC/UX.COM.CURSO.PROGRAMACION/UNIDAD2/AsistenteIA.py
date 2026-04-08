# AsistenteIA.py

# Simulación de un asistente de inteligencia artificial que procesa instrucciones con diferentes niveles de confianza.
UMBRAL_ALTO = 80.0
UMBRAL_MINIMO = 40.0

# Solicitar al usuario que ingrese una instrucción y el nivel de confianza calculado.
instruccion = input("Instrucción recibida: ")

# Simulación de cálculo de confianza (en un escenario real, esto sería generado por un modelo de IA).
confianza_str = input("Nivel de confianza calculado (%): ")

# Convertir la entrada de confianza a un número flotante.
confianza = float(confianza_str)

# Evaluar la confianza y responder en consecuencia.
if confianza >= UMBRAL_ALTO:
    print(f"Ejecutando la acción: [{instruccion}]... (Éxito)")

elif confianza >= UMBRAL_MINIMO:
    print(f"Confianza insuficiente. ¿Se refiere a: [{instruccion}]? Por favor confirme.")

elif confianza < UMBRAL_MINIMO:
    print(f"Error 404: No pude entender la instrucción. Intente hablar más claro.")

else:
    confianza > 95.0
    print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

# Simulación de finalización del procesamiento.
print("Sesión de procesamiento finalizada.")