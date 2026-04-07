# Escribe un programa que solicite al usuario ingresar números enteros. El programa debe sumar los números ingresados que estén entre 10 y 50 (inclusive). Si el usuario ingresa un número fuera de ese rango, el programa debe mostrar la suma total acumulada hasta ese momento y finalizar.
def main():
    suma = 0
    # El programa utiliza un bucle infinito para solicitar al usuario ingresar números enteros. Dentro del bucle, se verifica si el número ingresado está entre 10 y 50 (inclusive). Si es así, se suma a la variable "suma". Si el número está fuera de ese rango, se muestra la suma acumulada y el programa termina.
    while True:
        numero = int(input("Ingrese un número: "))
        if 10 <= numero <= 50:
            suma += numero
        else:
            print("Suma:", suma)
            break
# El programa solicita al usuario ingresar números enteros. Si el número ingresado está entre 10 y 50 (inclusive), se suma a la variable "suma". Si el número está fuera de ese rango, se muestra la suma acumulada hasta ese momento y el programa finaliza.
if __name__ == "__main__":
    main()