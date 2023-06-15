import csv
import matplotlib.pyplot as plt

# Nombre del archivo CSV de entrada
nombre_archivo_csv = "datos_filtrados.csv"

# Listas para almacenar los datos de amplitud
amplitudes = []

# Leer el archivo CSV y almacenar los datos de amplitud
with open(nombre_archivo_csv, 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    next(lector_csv)  # Saltar el encabezado del archivo
    
    for fila in lector_csv:
        amplitud_db = float(fila[0])
        amplitudes.append(amplitud_db)

# Graficar la distribución de amplitud con ejes logarítmicos
plt.hist(amplitudes, bins=10, log=True)
plt.xlabel('Amplitud (dB)')
plt.ylabel('Frecuencia de Amplitud')
plt.title('Distribución de Amplitud')

plt.xlim(xmin=-1000, xmax=-80)
plt.show()
