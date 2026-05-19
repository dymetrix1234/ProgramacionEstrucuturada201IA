# 1. IMPORTACIÓN  
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso 
import numpy as np 

def procesar_estadisticas(lista_mensajes): 
    """ 
    Función que recibe datos y utiliza funciones externas de  
    la biblioteca NumPy para procesarlos. 
    """ 
    # Invocación de función externa para el promedio 
    promedio = np.mean(lista_mensajes) 
    # Invocación de función externa para encontrar el valor máximo 
    pico_maximo = np.max(lista_mensajes) 
    # Invocación de función externa para la desviación estándar 
    desviacion = np.std(lista_mensajes)
    #Invocacion de funcion externa para la madiana
    madiana = np.median(lista_mensajes)
    return promedio, pico_maximo, desviacion, madiana

def main():
    # --- Programa Principal ---
    # Datos: Mensajes enviados cada hora durante un turno de 8 horas
    datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]
    # Llamada a nuestra función enviando los parámetros de entrada
    prom, maximo, ds, mediana = procesar_estadisticas(datos_servidor)
    print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
    print(f"Promedio de mensajes por hora: {prom:.2f}")
    print(f"Pico de actividad registrado: {maximo} mensajes")
    print(f"Variabilidad del tráfico (Desviación): {np.round(ds, 2)}")
    print(f"Mediana del tráfico: {mediana:.2f}")

if __name__ == "__main__":
    main()

    #AL NO PONER EL IMPORT AL INICIO, SALTA EL SIGUIENTE ERROR:
        #M.CURSO.PROGRAMACION\UNIDAD4\practica01\analisis_mensajes.py", line 33, in <module>
        #main()
        #~~~~^^
    #File "c:\Users\Dymet\OneDrive\Documentos\ProgramacionEstrucuturada201IA\SRC\UX.COM.CURSO.PROGRAMACION\UNIDAD4\practica01\analisis_mensajes.py", line 25, in main
        #prom, maximo, ds, mediana = procesar_estadisticas(datos_servidor)
                                    #~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
    #File "c:\Users\Dymet\OneDrive\Documentos\ProgramacionEstrucuturada201IA\SRC\UX.COM.CURSO.PROGRAMACION\UNIDAD4\practica01\analisis_mensajes.py", line 11, in procesar_estadisticas
        #promedio = np.mean(lista_mensajes)
                #^^
    #NameError: name 'np' is not defined