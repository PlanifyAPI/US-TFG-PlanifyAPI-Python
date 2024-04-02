import re
import os

# Directorio que contiene los archivos de logs
directorio_logs = '../tfg/log/amadeus__r_ft_/log.json'

# Función para leer y filtrar los archivos de logs
def filtrar_logs(archivo):
    with open(archivo, 'r') as f:
        with open('requests.log', 'w') as f_out:
            for linea in f:
                print(linea)
                if "GET" in linea or "HTTP/1.1" in linea:
                    f_out.write(linea)

# Recorrer todos los archivos en el directorio de logs
for archivo in os.listdir(directorio_logs):
    ruta_archivo = os.path.join(directorio_logs, archivo)
    if os.path.isfile(directorio_logs):
        filtrar_logs(directorio_logs)
