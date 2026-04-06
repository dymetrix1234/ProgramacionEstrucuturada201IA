#calcula numeros impares hasta el número ingresado por el usuario

# Leer N
N = int(input("Ingrese un número: "))

# Inicializar variables
contador = 0
numero = 1

# Bucle para calcular los números impares
while contador < N:
    print(numero)
    numero = numero + 2
    contador = contador + 1

# Mostrar el resultado
print("Fin del programa")