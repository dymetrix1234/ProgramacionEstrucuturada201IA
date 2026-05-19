print("--- SISTEMA DE CONTROL BIOMÉTRICO ---\n")

nombre = input("Nombre del Ingeniero: ").strip()

try:
    empleado_id = int(input("ID de Empleado: ").strip())
except ValueError:
    print("ID inválido. Por favor ingrese un número entero para el ID de empleado.")
    raise

iris = input("¿El escaneo de Iris coincide? (si/no): ").strip().lower()
facial = input("¿El reconocimiento facial es > 95%? (si/no): ").strip().lower()

acceso_concedido = False

if empleado_id <= 0:
    print("\n¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")
elif iris == "si" and facial == "si":
    if empleado_id < 100:
        print(f"\n> Diagnóstico: Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
        acceso_concedido = True
    else:
        print(f"\n> Diagnóstico: Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
        acceso_concedido = True
else:
    print("\n> Diagnóstico: Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

if acceso_concedido:
    print(f"Generando log de entrada para el usuario: {empleado_id}...")
