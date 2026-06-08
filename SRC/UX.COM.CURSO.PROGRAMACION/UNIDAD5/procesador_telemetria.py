# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# PEGA AQUÍ LAS 3 FUNCIONES GENERADAS POR IA
# ==========================================
def limpiar_lecturas(lista_datos):
    """Filtra las lecturas de telemetría eliminando valores fuera del rango válido.
    Parámetros:
        lista_datos (list): Lista de números flotantes con lecturas LIDAR.
    Retorna:
        list: Lista con las lecturas válidas entre 0.0 y 100.0 inclusive.
    """
    lista_filtrada = []
    if isinstance(lista_datos, list):
        for lectura in lista_datos:
            if isinstance(lectura, (int, float)):
                if 0.0 <= lectura <= 100.0:
                    lista_filtrada.append(lectura)
    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """Cuenta cuántas lecturas están por debajo del umbral crítico.
    Parámetros:
        lista_filtrada (list): Lista de lecturas válidas.
        umbral_critico (float): Valor de umbral para riesgo de colisión.
    Retorna:
        int: Cantidad de alertas detectadas.
    """
    total_alertas = 0
    if isinstance(lista_filtrada, list):
        for lectura in lista_filtrada:
            if isinstance(lectura, (int, float)):
                if lectura < umbral_critico:
                    total_alertas += 1
    return total_alertas


def generar_log_sistema(total_alertas):
    """Genera un mensaje de log con el sistema operativo y la acción recomendada.
    Parámetros:
        total_alertas (int): Número de alertas críticas detectadas.
    Retorna:
        str: Cadena formateada con el sistema y la decisión.
    """
    sistema = sys.platform
    if sistema.startswith("win"):
        nombre_sistema = "Windows"
    elif sistema.startswith("darwin"):
        nombre_sistema = "macOS"
    elif sistema.startswith("linux"):
        nombre_sistema = "Linux"
    else:
        nombre_sistema = sistema

    accion = "ABORTAR" if isinstance(total_alertas, int) and total_alertas > 3 else "PERMITIDA"
    return f"[{nombre_sistema}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # 1. Datos de prueba simulados (telemetría LIDAR)
    # Incluye lecturas válidas, un valor negativo (-5.0) y uno mayor a 100 (120.5) que deben ser descartados
    lecturas_crudas = [45.2, 12.5, -5.0, 88.1, 5.3, 120.5, 2.1, 9.4, 75.0]
    umbral = 15.0  # Valores por debajo de 15.0 se consideran de riesgo

    print("--- INICIANDO SISTEMA DE TELEMETRÍA ---")
    print(f"Lecturas originales: {lecturas_crudas}")
    print(f"Umbral crítico establecido: {umbral}\n")

    # 2. Paso 1: Filtrar y limpiar los datos de la lista
    datos_limpios = limpiar_lecturas(lecturas_crudas)
    print(f"[PASO 1] Lecturas filtradas (0.0 a 100.0): {datos_limpios}")

    # 3. Paso 2: Contar las alertas según el umbral crítico
    alertas_detectadas = calcular_alertas(datos_limpios, umbral)
    print(f"[PASO 2] Total de alertas de riesgo detectadas: {alertas_detectadas}")

    # 4. Paso 3: Generar el informe final (log) del sistema
    resultado_log = generar_log_sistema(alertas_detectadas)
    
    print("\n--- REPORTE FINAL DEL LOG ---")
    print(resultado_log)

    """
    Prompt: En base a el siguiente codigo base, genera las partes que estan marcadas como "PARA IA"
    Tabla de Prueba de Escritorio Manual (Trace Table)Para este caso, diseñaremos un escenario extremo:
    Una lista donde absolutamente todas las lecturas son erróneas (ya sea por tipo de dato incorrecto o por estar fuera del rango lógico de $0.0$ a $100.0$).Configuración del Caso de Pruebalecturas_crudas = [-10.5, "error", 150.0]umbral = 10.0Flujo Paso a Paso (Explicación Textual)Inicio del Bloque Principal: Se asignan las variables iniciales lecturas_crudas y umbral.Llamada a limpiar_lecturas(lista_datos):La variable local lista_datos recibe [-10.5, "error", 150.0].Se inicializa lista_filtrada = [].Iteración 1: lectura = -10.5. Es un número, pero no cumple la condición 0.0 <= lectura <= 100.0. No se añade a la lista.Iteración 2: lectura = "error". No pasa el filtro isinstance(lectura, (int, float)). No se añade.Iteración 3: lectura = 150.0. Es un número, pero supera el límite de $100.0$. No se añade.La función retorna una lista vacía: [].Llamada a calcular_alertas(lista_filtrada, umbral_critico):La variable local lista_filtrada recibe [] y umbral_critico recibe 10.0.Se inicializa total_alertas = 0.El ciclo for no se ejecuta porque la lista está vacía.La función retorna 0.Llamada a generar_log_sistema(total_alertas):Recibe total_alertas = 0.Detecta el sistema operativo (por ejemplo, Windows).Evalúa la condición de la acción: como total_alertas ($0$) no es mayor que $3$, la variable accion toma el valor "PERMITIDA".Retorna el mensaje de log formateado.Representación en Tabla de SeguimientoLínea / PasoVariable lecturaCondición (Rango / Tipo)Variable lista_filtradaVariable total_alertasVariable accionRetorno / ResultadoInicioNingunaNingunaNo creadaNo creadaNo creadaSe definen datos de pruebaFunc 1 - It. 1-10.5Falso (Fuera de rango)[]No aplicaNo aplicaSigue el cicloFunc 1 - It. 2"error"Falso (Tipo incorrecto)[]No aplicaNo aplicaSigue el cicloFunc 1 - It. 3150.0Falso (Fuera de rango)[]No aplicaNo aplicaTermina ciclo. Retorna []Func 2No aplicaLista vacía, no iteraRecibe []0No aplicaTermina. Retorna 0Func 3No aplica0 > 3 es FalsoNo aplica0"PERMITIDA"Retorna Log Final2. Auditoría de CódigoAnalizando las tres funciones proporcionadas en tu plantilla, realizamos la siguiente evaluación respecto a las reglas de la programación estructurada básica:¿La IA intentó utilizar sintaxis avanzada o bibliotecas externas?No de manera crítica, pero al borde de lo avanzado. La IA se mantuvo dentro de la biblioteca estándar de Python al usar únicamente import sys (permitido para detectar el sistema operativo). Tampoco utilizó try-except (control de excepciones) ni list comprehensions (comprensión de listas), lo cual es excelente porque esos temas suelen ser de un nivel intermedio/avanzado.Sin embargo, implementó un par de elementos que podrían no haberse visto aún en clases introductorias:La función isinstance(): Utilizada para validar si los datos son estrictamente numéricos (int o float) o listas. En un nivel muy básico, se suele asumir que los datos de entrada ya son correctos o se limpia la lista usando simplemente comparaciones directas.Operador Ternario: En la tercera función, la IA usó una estructura en una sola línea:accion = "ABORTAR" if ... else "PERMITIDA".¿Cómo se modifica el prompt o el código para forzar un diseño más básico?Si tu profesor exige un diseño puramente estructurado, plano y de nivel escolar, se debe modificar el código (o guiar a la IA con un prompt específico) de la siguiente manera:Prompt correctivo para la IA:"Genera el código utilizando únicamente estructuras de control básicas (if/elif/else, ciclos for tradicionales). No utilices la función isinstance(), asume que la lista contiene números. No utilices asignaciones condicionales en una sola línea (operadores ternarios); desglosa los if-else en bloques sangrados estándar."Modificación directa en el código (Ejemplo de simplificación):Python# ASÍ LO HIZO LA IA (Avanzado/Robusto):
    accion = "ABORTAR" if isinstance(total_alertas, int) and total_alertas > 3 else "PERMITIDA"

    # ASÍ SE MODIFICA PARA MANTENERLO BÁSICO (Estructurado tradicional):
if total_alertas > 3:
    accion = "ABORTAR"
else:
    accion = "PERMITIDA"
    """