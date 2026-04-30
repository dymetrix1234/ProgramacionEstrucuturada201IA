class ControlAcceso:
    def __init__(self):
        # Diccionario inicial de usuarios autorizados
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía.")

        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None

    def registrar_nuevo_usuario(self):
        print("\n--- Registro de Nuevo Usuario (Modo Administrador) ---")
        nueva_id = input("Ingrese la nueva matrícula: ")
        nuevo_rol = input("Ingrese el rol (Estudiante/Investigador/etc): ")
        
        if nueva_id and nuevo_rol:
            self.usuarios_autorizados[nueva_id] = nuevo_rol
            print(f"Usuario {nueva_id} registrado exitosamente.")
        else:
            print("Error: Datos incompletos, registro cancelado.")

# --- Flujo Principal ---
sistema = ControlAcceso()
print("--- Sistema de Seguridad Laboratorio IA - UX ---")

while True:
    try:
        matricula_input = input("\nIngrese su matrícula (o 'salir' para terminar): ")
        
        if matricula_input.lower() == 'salir':
            break

        rol_activo = sistema.verificar_permisos(matricula_input)

        # Funcionalidad Extra: Si es Administrador, puede agregar usuarios
        if rol_activo == "Administrador":
            opcion = input("¿Desea registrar un nuevo usuario? (s/n): ")
            if opcion.lower() == 's':
                sistema.registrar_nuevo_usuario()

    except ValueError as e:
        print(f"Error de entrada: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        print("--- Intento de acceso registrado en el log del servidor ---")