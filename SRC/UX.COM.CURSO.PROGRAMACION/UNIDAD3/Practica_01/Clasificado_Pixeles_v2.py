'''
Version 2 del clasificador de pixeles para cargar una fuente
'''

#Limpiez de datos, normalizacion

# ClasificadoPixeles.py
from ast import Return


def main():
    cargar_y_procesar("lectura_sensores.txt")

# Declaracion de constantes
UMBRAL_BAJO = 0.3
UMBRAL_ALTO = 0.7

def clasificar_pixel(intensidad):
    #Si la intensidad es menor a 0.0 o mayor a 1.0 es un valor invalido
    if intensidad < 0.0 or intensidad > 1.0:
        return None
    
    #Clasificacion del pixel
    if 0.0 <= intensidad <= UMBRAL_BAJO:
        return("Fodo oscuro")

    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        return("Gris (Ruido)")

    if intensidad >= UMBRAL_ALTO:
        return("Objeto (brillante)")

    return("Analisis de imagen finalizado.")

import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0

    #obtener la ruta del archivo
    ruta_archivo = os.path.dirname(__file__)
    ruta_archivo = os.path.join(ruta_archivo, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                #convertir cada linea a un numero flotante
                valor_crudo = float(linea.strip())

                #clasificar el valor del pixel
                clasificacion = clasificar_pixel(valor_crudo)

                #Agregamos la logica de clasis=ficacion
                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append (clasificacion)
                    if clasificacion == "Fondo oscuro":
                        fondo_oscuro += 1
                    elif clasificacion == "Gris (Ruido)":
                        gris_ruido += 1
                    elif clasificacion == "Objeto (brillante)":
                        objeto_brillante += 1

        print(f"Ruido detectado: {ruido_detectado}")
        print(f"Fondo oscuro: {fondo_oscuro}")
        print(f"Gris (Ruido): {gris_ruido}")
        print(f"Objeto (brillante): {objeto_brillante}")
    except FileNotFoundError:
        print(f"error:el archivo '{nombre_archivo}' no se encontro.")
    
    

if __name__ == "__main__":
    main()


#Módulo de clasificación de píxeles para análisis de imágenes.
#Este módulo proporciona funcionalidades para cargar datos de sensores desde un archivo,
#normalizar los valores de intensidad de píxeles y clasificarlos en categorías basadas
#en umbrales predefinidos.
#Constantes:
#    UMBRAL_BAJO (float): Umbral inferior para clasificación de píxeles (0.3)
#    UMBRAL_ALTO (float): Umbral superior para clasificación de píxeles (0.7)
#Funciones:
#    main(): Función principal que inicia el proceso de carga y procesamiento
#    clasificar_pixel(intensidad: float) -> str | None:
#        Clasifica un píxel según su intensidad en las categorías:
#        - "Fondo oscuro": intensidad entre 0.0 y UMBRAL_BAJO
#        - "Gris (Ruido)": intensidad entre UMBRAL_BAJO y UMBRAL_ALTO
#        - "Objeto (brillante)": intensidad >= UMBRAL_ALTO
#        - None: si la intensidad está fuera del rango [0.0, 1.0]
#        Args:
#            intensidad (float): Valor de intensidad del píxel (0.0 a 1.0)
#        Returns:
#            str | None: Clasificación del píxel o None si es inválido
#    cargar_y_procesar(nombre_archivo: str) -> None:
#        Carga datos de un archivo de sensores, clasifica cada píxel y genera
#        estadísticas de clasificación. Maneja errores de archivo no encontrado.
#        Args:
#            nombre_archivo (str): Nombre del archivo a procesar
#        Imprime:
#            - Cantidad de ruido detectado (valores inválidos)
#            - Cantidad de píxeles de fondo oscuro
#            - Cantidad de píxeles grises (ruido)
#            - Cantidad de píxeles brillantes (objetos)
#Clasificación por funciones:
#     main() - PUNTO DE ENTRADA
#     clasificar_pixel() - LÓGICA DE CLASIFICACIÓN
#     cargar_y_procesar() - E/S Y PROCESAMIENTO