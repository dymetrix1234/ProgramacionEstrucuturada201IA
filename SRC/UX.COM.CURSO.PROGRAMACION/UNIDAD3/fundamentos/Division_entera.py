def division_artesanal(dividendo, divisor):
    # Validación básica para evitar bucles infinitos o errores
    if divisor == 0:
        return "Error: No se puede dividir por cero."
    
    cociente = 0
    # Trabajamos con valores absolutos para la lógica de resta
    resto = abs(dividendo)
    divisor_abs = abs(divisor)
    
    # Proceso de restas sucesivas
    while resto >= divisor_abs:
        resto -= divisor_abs
        cociente += 1
        
    if (dividendo < 0) ^ (divisor < 0):
        cociente = -cociente
        
    return cociente, resto

dividendo = 17
divisor = 3
c, r = division_artesanal(dividendo, divisor)

print(f"Resultado de {dividendo} / {divisor}:")
print(f"Cociente: {c}")
print(f"Resto: {r}")