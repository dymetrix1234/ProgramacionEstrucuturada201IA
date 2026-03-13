def Dias():
    print("-- Dias --")
    opcion = input("ingrese una opcion (1-7):")

    match opcion:
        case "1":
            print("Lunes")
        case "2":
            print("Martes")
        case _:
            print ("opcion no valida") 

def main():
    Dias()
if __name__ == "__main__":
    main()
