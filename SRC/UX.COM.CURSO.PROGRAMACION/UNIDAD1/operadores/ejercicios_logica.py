#ejercicio de operadores logicos
def operadores():
    a = True
    b = False

    print (a and b)
    print (a or b)
    print (not a)
    print (not b)

    numero_1 = 10
    numero_2 = 20

    if numero_1 > numero_2:
        print("numrto 1 es mayor que numero 2")
    else:
        print("numero 1 es menor que numero 2")

def main():
    operadores()

if __name__ == "__main__":
    main()