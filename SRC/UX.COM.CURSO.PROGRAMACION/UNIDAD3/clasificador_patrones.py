puntajes_sentimiento = [0, 0, 0]

print("--- ANALIZADOR DE SENTIMIENTOS IA ---\n")

for i in range(5):
    while True:
        try:
            respuesta = int(input(f"Palabra {i+1} - Clasificación (0, 1, 2): "))
            if respuesta in (0, 1, 2):
                break
            print("Por favor ingresa 0, 1 o 2.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero 0, 1 o 2.")

    puntajes_sentimiento[respuesta] += 1
    print()

mayor_indice = 0
for indice in range(1, len(puntajes_sentimiento)):
    if puntajes_sentimiento[indice] > puntajes_sentimiento[mayor_indice]:
        mayor_indice = indice

print("Estado final del vector de características:", puntajes_sentimiento)

if mayor_indice == 0:
    print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")
elif mayor_indice == 1:
    print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")
else:
    print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")
