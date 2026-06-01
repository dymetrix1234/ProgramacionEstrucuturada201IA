# Declaración de estructuras
def main():
	productos = ["Laptop", "Smartphone", "Tablet"]
	dias = ["Lunes", "Martes", "Miércoles"]
	ventas = [[0] * 3 for _ in range(3)]

	print("Registro de ventas para 3 productos y 3 días (Lunes, Martes, Miércoles)")
	for i in range(3):
		print(f"--- Registro para {productos[i]} ---")
		for j in range(3):
			while True:
				try:
					valor = input(f"Ingrese ventas de {productos[i]} para {dias[j]} (día {j+1}): ")
					numero = int(valor)
					if numero < 0:
						print("El valor no puede ser negativo. Intente de nuevo.")
						continue
					ventas[i][j] = numero
					break
				except ValueError:
					print("Entrada no válida. Ingrese un número entero.")

	# Escritura: tabla organizada
	print("\nRESUMEN DE VENTAS")
	encabezado = "Producto\t" + "\t".join(dias) + "\tTotal"
	print(encabezado)
	total_general = 0
	totales_por_producto = []

	for i in range(3):
		suma_producto = sum(ventas[i])
		totales_por_producto.append(suma_producto)
		total_general += suma_producto
		fila_vals = "\t".join(str(v) for v in ventas[i])
		print(f"{productos[i]}\t{fila_vals}\t{suma_producto}")

	promedio = total_general / (3 * 3)
	print(f"\nEl total de ventas de la semana es: {total_general}")
	print(f"El promedio de ventas por día (todos los productos): {promedio:.2f}")

	# Producto más vendido
	max_ventas = max(totales_por_producto)
	indices = [i for i, t in enumerate(totales_por_producto) if t == max_ventas]
	if len(indices) == 1:
		print(f"El producto más vendido de la semana fue: {productos[indices[0]]} con {max_ventas} unidades.")
	else:
		productos_empate = ", ".join(productos[i] for i in indices)
		print(f"Hubo empate como más vendidos: {productos_empate} con {max_ventas} unidades cada uno.")


if __name__ == "__main__":
	main()

productos = ["Laptop", "Smartphone", "Tablet"]

ventas = [[0] * 3 for _ in range(3)]

 

# Lectura de datos

for i in range(3):

    print(f"--- Registro para {productos[i]} ---")

    for j in range(3):

        ventas[i][j] = int(input(f"Ventas del día {j+1}: "))

 

# Escritura y Reporte

print("\nRESUMEN DE VENTAS")

total_general = 0

 

for i in range(3):

    suma_producto = sum(ventas[i])

    total_general += suma_producto

    print(f"{productos[i]}: {ventas[i]} | Total: {suma_producto}")

 

print(f"\nEl total de ventas de la semana es: {total_general}")

print(f"El promedio de ventas es: {total_general / 9:.2f}")