import csv

# Nombre del archivo CSV de entrada
nombre_archivo_csv = "datos_amplitud.csv"

# Nombre del archivo de salida
nombre_archivo_salida = "muestras_bajas.csv"

# Leer el archivo CSV
with open(nombre_archivo_csv, 'r') as archivo_csv, open(nombre_archivo_salida, 'w', newline='') as archivo_salida:
    lector_csv = csv.reader(archivo_csv)
    escritor_csv = csv.writer(archivo_salida)
    
    # Escribir el encabezado en el archivo de salida
    escritor_csv.writerow(next(lector_csv))
    
    # Iterar sobre las filas del archivo CSV
    for fila in lector_csv:
        amplitud_db = float(fila[0])
        tiempo = float(fila[1])
        
        # Verificar si la amplitud es menor a -80 dB
        if amplitud_db < -80:
            # Escribir la fila en el archivo de salida
            escritor_csv.writerow([amplitud_db, tiempo])
