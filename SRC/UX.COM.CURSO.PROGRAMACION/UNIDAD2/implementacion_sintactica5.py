# Implementación sintáctica de un sistema de verificación de contraseña con límite de intentos.

# El programa solicita al usuario que ingrese una contraseña y verifica si es correcta. Si la contraseña es incorrecta, se incrementa el contador de intentos. Si el usuario alcanza el límite de 3 intentos, la cuenta se bloquea.
def verificar_acceso():
    """
    Sistema de verificación de contraseña con límite de intentos.
    Máximo 3 intentos antes de bloquear la cuenta.
    """


    intentos = 0
    clave_correcta = '1234'
    
    # El bucle se ejecuta mientras el número de intentos sea menor que 3
    while intentos < 3:
        contrasena = input("Ingrese la contraseña: ")
        
        if contrasena == clave_correcta:
            print("Acceso Concedido")
            return
        else:
            intentos += 1
            print("Contraseña incorrecta")
    
    print("Cuenta bloqueada")

# Punto de entrada del programa
if __name__ == "__main__":
    verificar_acceso()