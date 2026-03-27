# A. Inicio e Inicialización (Nodo B)
suma = 0
i = 1

# B. Condición de parada (Nodo C)
# Mientras i sea menor o igual a 100, el flujo sigue por "Sí"
while i <= 100:
    
    # C. Condición lógica compuesta (Nodo D)
    # ¿Es divisible por 3 Y es impar?
    if i % 3 == 0 and i % 2 != 0:
        # D. Acumulador (Nodo E)
        # Solo se ejecuta si la condición de D es verdadera
        suma = suma + i
    
    # E. Incremento del contador (Nodo F)
    # Note que este paso ocurre siempre, ya sea que D sea Sí o No
    i = i + 1

# F. Salida de datos (Nodo G)
# Cuando la condición de C es "No", se muestra el resultado
print("La suma de los números impares divisibles por 3 entre 1 y 100 es:", suma)

# G. Fin (Nodo H)