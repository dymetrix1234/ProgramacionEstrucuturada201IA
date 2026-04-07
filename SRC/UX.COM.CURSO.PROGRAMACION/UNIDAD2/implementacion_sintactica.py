#definir una función main que solicite al usuario ingresar números hasta que la suma de los números ingresados sea mayor a 500. La función debe manejar excepciones para asegurarse de que el usuario ingrese solo números válidos.
def main():
    suma = 0
    # Bucle para solicitar números hasta que la suma sea mayor a 500
    while suma <= 500:
        try:
            numero = float(input("Ingrese un número: "))
        except ValueError:
            print("Valor no válido. Intente de nuevo.")
            continue

        suma += numero

    print("Suma =", suma)
# Fin del programa
if __name__ == "__main__":
    main()