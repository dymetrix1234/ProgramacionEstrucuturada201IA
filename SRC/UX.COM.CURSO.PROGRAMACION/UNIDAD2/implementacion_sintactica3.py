# Implementación sintáctica 3: Acumulador y condición de salida
saldo = 0
meta = 1000
# El programa utiliza un bucle "while" para solicitar al usuario ingresar montos de depósito. El bucle continúa ejecutándose mientras el saldo acumulado sea menor o igual a la meta establecida. Dentro del bucle, se solicita al usuario ingresar el monto del depósito, que se suma al saldo acumulado. Una vez que el saldo supera la meta, el programa muestra un mensaje indicando que la meta ha sido superada y muestra el saldo final.
while saldo <= meta:
    deposito = float(input("Ingrese el monto del depósito: "))
    saldo += deposito
# El programa solicita al usuario ingresar montos de depósito y los acumula en la variable "saldo". El bucle continúa ejecutándose mientras el saldo acumulado sea menor o igual a la meta establecida. Una vez que el saldo supera la meta, se muestra un mensaje indicando que la meta ha sido superada y se muestra el saldo final.
print("Meta superada")
print(f"Saldo: {saldo}")