#ejemplo para visualizar la identacion en python

def explicar_identacion():
    #nivel 1
    mensaje = "nivel 1 de identacion"
    print(mensaje)

    puntos = 10

    if puntos > 9:
        #nivel 2
        print ("entra al flujo del if")

        if puntos == 10:
            #nivel 3
            print("puntos es igual a 10")

# cierra nivel 1
def main():
    explicar_identacion()

if __name__ == "__main__":
    main()