from pydub import AudioSegment

def obtener_datos_mp3(ruta_archivo="."):
    audio = AudioSegment.from_file(ruta_archivo, format="wav")
    
    # Obtener la duración del archivo en segundos
    duracion_segundos = len(audio) / 1000
    
    # Obtener la frecuencia de muestreo en Hz
    frecuencia_muestreo = audio.frame_rate
    
    return duracion_segundos, frecuencia_muestreo

ruta_archivo = "tipo_largo_fino.wav"
duracion, frecuencia = obtener_datos_mp3(ruta_archivo)

print("Duración:", duracion, "segundos")
print("Frecuencia de muestreo:", frecuencia, "Hz")
print("")