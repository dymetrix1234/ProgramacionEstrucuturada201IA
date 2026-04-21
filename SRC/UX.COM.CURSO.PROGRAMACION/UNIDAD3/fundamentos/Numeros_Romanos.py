def numero_decimal():
    return int(input("Ingrese un número decimal entero: "))

def convertir_a_romano(numero):
    if numero < 1 or numero > 3999:
        return "Número fuera de rango (1-3999)"
    
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
            
    return resultado