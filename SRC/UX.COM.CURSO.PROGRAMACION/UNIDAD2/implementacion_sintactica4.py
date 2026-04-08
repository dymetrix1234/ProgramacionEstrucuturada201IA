#porgrama para calcular el numero de semanas necesarias para alcanzar una meta de ahorro
total_acumulado = 0
semanas = 0
meta = 2500

#bucle para acumular el total hasta alcanzar la meta
while total_acumulado < meta:
    # Solicitar salario semanal al usuario
    salario_semanal = float(input("Ingrese salario semanal: "))
    
    # total acumulado se incrementa con el salario semanal
    total_acumulado = total_acumulado + salario_semanal
    
    # Incrementar el contador de semanas
    semanas = semanas + 1

# Imprimir el número de semanas necesarias para alcanzar la meta
print("Semanas trabajadas: " + str(semanas))