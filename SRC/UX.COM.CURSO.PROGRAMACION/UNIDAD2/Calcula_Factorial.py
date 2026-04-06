# Calcula_Factorial.py

# Leer N
N = int(input("Ingrese el valor de N: "))

# Inicializar variables
factorial = 1
i = 1

# Bucle para calcular el factorial
while i <= N:
    factorial = factorial * i
    i = i + 1

# Mostrar el resultado
print(f"El factorial de {N} es: {factorial}")