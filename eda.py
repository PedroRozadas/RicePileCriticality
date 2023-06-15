import csv
import wave
import numpy as np
import matplotlib.pyplot as plt

# Nombre del archivo WAV de entrada
nombre_archivo = "tipo_largo_fino.wav"

# Abrir el archivo WAV
with wave.open(nombre_archivo, 'rb') as archivo_wav:
    # Obtener los parámetros del archivo WAV
    n_channels = archivo_wav.getnchannels()
    sample_width = archivo_wav.getsampwidth()
    frame_rate = archivo_wav.getframerate()
    n_frames = archivo_wav.getnframes()

    # Leer todos los frames del archivo WAV
    frames = archivo_wav.readframes(n_frames)

    # Convertir los frames a un array de valores
    muestras = np.frombuffer(frames, dtype=np.int16)

    # Calcular el tiempo de cada muestra
    tiempos = np.arange(0, n_frames) / frame_rate

    plt.plot(tiempos, muestras)
    print(muestras)


    plt.show()
    # Calcular la amplitud en decibelios de cada muestra
    amplitud_db = 20 * np.log10(np.abs(muestras) / (2 ** (sample_width * 8 - 1)))

    # # Crear un archivo CSV y escribir los datos
    # with open("datos_amplitud.csv", 'w', newline='') as archivo_csv:
    #     escritor_csv = csv.writer(archivo_csv)
    #     escritor_csv.writerow(['Amplitud (dB)', 'Tiempo (s)'])
    #     for i in range(len(amplitud_db)):
    #         escritor_csv.writerow([amplitud_db[i], tiempos[i]])
