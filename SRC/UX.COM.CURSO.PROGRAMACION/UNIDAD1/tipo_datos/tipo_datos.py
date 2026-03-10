def datos():

    # demostracion de tipos de datos en python
    entero = 25
    decimal = 3.14
    cadena = "Hola, mundo!"
    boleano = True

    print(entero)
    print(decimal)
    print(cadena)
    print(boleano)

def tipos_datos_compuesto():
    lista = [10, 20, 30, 40]
    tupla = (19, 29, 39, 49)
    diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

    print(lista)
    print(tupla)
    print(diccionario)

def main():
    datos()
    tipos_datos_compuesto()

if __name__ == "__main__":
    main()