from pydub import AudioSegment
import librosa
import wave
import numpy as np
import matplotlib.pyplot as plt

def obtener_datos_mp3(ruta_archivo):
    audio = AudioSegment.from_file(ruta_archivo, format="wav")
    
    # Obtener la duración del archivo en segundos
    # Length audio in milliseconds, so dividing it by 1000 gives the duration in seconds
    duracion_segundos = len(audio) / 1000
    
    # Obtener la frecuencia de muestreo en Hz
    frecuencia_muestreo = audio.frame_rate

    intensidad = audio.dBFS
    
    return duracion_segundos, frecuencia_muestreo, intensidad

ruta_archivo = "tipo_largo_fino.wav"
duracion, frecuencia, intensidad = obtener_datos_mp3(ruta_archivo)

print("Duración:", duracion, "segundos")
print("Frecuencia de muestreo:", frecuencia, "Hz")
print("Intensidad", intensidad, "dB")
def amplitude(audio_path):
    # Open wav file and read frames as bytes
    sf_filewave = wave.open(audio_path, 'r')
    signal_sf = sf_filewave.readframes(-1)
    # Convert audio bytes to integers
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')
    # Get the sound wave frame rate
    framerate_sf = sf_filewave.getframerate()
    # Find the sound wave timestamps
    time_sf = np.linspace(start=0,
                        stop=len(soundwave_sf)/framerate_sf,
                        num=len(soundwave_sf))
    # Filter soundwave_sf and time_sf based on the threshold
    threshold = 3000
    filtered_soundwave_sf = soundwave_sf[soundwave_sf >= threshold]
    filtered_time_sf = time_sf[soundwave_sf >= threshold]
    # Set up plot
    f, ax = plt.subplots(figsize=(15, 3))
    # Setup the title and axis titles
    plt.title('Amplitude over Time')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (seconds)')
    # Add the audio data to the plot
    ax[0] = plt.plot(time_sf, soundwave_sf, label='Warm Memories', alpha=0.5)
    plt.legend()
    plt.show()
    return
    
amplitude(ruta_archivo)
def apply_threshold(audio_path):
    audio, sr = librosa.load(audio_path)

    # Calculate the root mean square (RMS) of the audio
    rms = librosa.feature.rms(y=audio)

    # Convert RMS to decibels (dB)
    db = librosa.amplitude_to_db(rms, ref=np.max)

    # Set the desired dB threshold
    threshold_db = -20

    # Apply the threshold
    audio[np.where(db < threshold_db)] = 0

    # Save the modified audio to a new file
    modified_audio_path = 'path_to_modified_audio_file.wav'
    librosa.output.write_wav(modified_audio_path, audio, sr)
    
    return

