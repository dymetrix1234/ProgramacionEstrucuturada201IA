# Asistente lógico en Python

#Importamos el módulo datetime para obtener la hora actual del sistema
import datetime

# Definimos el nombre del asistente lógico
nombre_asistente = "Jarvis"

# Saludo inicial del asistente
print(f"Hola, soy {nombre_asistente}, tu asistente lógico. ¿En qué puedo ayudarte hoy?")

# Solicitamos al usuario que ingrese una frase y la convertimos a minúsculas para facilitar la comparación
frase = input("Por favor, ingresa una frase: ").lower()

# Evaluamos la frase ingresada por el usuario y respondemos según el contenido
if "hola" in frase or "buenos días" in frase:
    print("¡Hola! Soy tu asistente. Es un gusto saludarte.")
elif "clima" in frase or "temperatura" in frase:
    print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")
elif "hora" in frase or "tiempo" in frase:
    print(f"La hora actual del sistema es: {datetime.datetime.now().strftime('%H:%M:%S')}")
else:
    print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")

# Despedida del asistente
print(f"Proceso finalizado. Gracias por usar {nombre_asistente}.")