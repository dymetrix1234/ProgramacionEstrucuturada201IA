#desarrollo de lgoritmo contador de numeros positivos

def contador_positivos():
    contador = 0
    while True:
        numero = int(input("Ingrese un número (-1 para terminar): "))
        if numero <0:
            break
        contador += 1

    print(f"Cantidad de números positivos ingresados: {contador}")

'''
definicion de la funcion main (controla el flujo del programa)
'''

def main():
    print("bienvenido al contador de números positivos")
    contador_positivos()

#llamada a la función main para iniciar el programa 
if __name__ == "__main__":
    main()