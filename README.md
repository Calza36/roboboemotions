<div align="center">
    <h1>
    ROBOBOEMOTIONS
    </h1>
    <p>
    <img src="src\logo.png" alt="ROBOBOEMOTIONS Logo" style="width: 400px; height: 400px;">
    </p>
    <p>
    (Logo generated by DALL·E 3)
    </p>
    <a href="https://github.com/Calza36/roboboemotions"><img src="https://img.shields.io/badge/Python-3.8+-orange" alt="version"></a>

</div>

# Multimodal Emotion Recognition Library: Combining Facial Emotion Recognition and Speech Emotion Recognition.

## Guía
roboboemotions es una librería de Python diseñada para predecir emociones a partir de imágenes y audios, utilizando una aproximación multimodal mediante fusión por ponderación. Esta herramienta está optimizada para su uso con el robot educativo Robobo, facilitando la detección emocional en aplicaciones educativas.

## Características
- Predicción de emociones multimodal: Combina resultados de análisis de imágenes y audios, ponderando 60% imagen y 40% audio.
- Emociones combinadas: Agrupa las emociones angry, fear, sad y disgust en una sola emoción denominada Negativa cuando se utiliza el método multimodal.
- Detección de emociones individual: Permite el uso independiente de detección de emociones por imagen y por audio.
- Librerías subyacentes: Utiliza DeepFace para la detección de emociones por imagen y emotion2vec para la detección de emociones por audio.

### Emociones Detectadas:
- Emociones individuales (por imagen o audio):
  - angry
  - disgust
  - fear
  - happy
  - sad
  - surprise
  - neutral
- Emociones combinadas (multimodal):
  - happy
  - surprise
  - neutral
  - Negativa
##

## Instalar:
### Instalar desde PYPI (Recommended)
1. instala desde pypi para obtener todas las librerias requeridas:
```bash
pip install robobo-emotion
```
### Instalar desde github 
1. Clona este repositorio:
```bash
git clone https://github.com/Calza36/roboboemotions.git
```
2. Accede al repositorio local:
```bash
cd roboboemotions
```
3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```
##
## EJEMPLOS DE USO
### Predicción Multimodal
```python
from robobo_emotion import MultimodalEmotion

image_path = "examples\Anger.jpg"
audio_path = "examples\YAF_match_angry.wav"

# Crear una instancia de MultimodalEmotion
analizador = MultimodalEmotion(image_path, audio_path)

# Acceder a los resultados
print("Fusión de emociones:", analizador.fusion_emotion)
print("Emoción predominante:", analizador.predominant_emotion)
print("Combinacion de emociones:", analizador.emociones_agrupadas)
```

### Predicción por Imagen
```python
from robobo_emotion import EmotionImage

image_path = "examples\Anger.jpg"
emotion_image = EmotionImage(image_path)
emotion = emotion_image.get_emotion()

print(emotion)
```

### Predicción por Audio
```python
from robobo_emotion import EmotionAudio

audio_path = "examples\YAF_match_angry.wav"
emotion_audio = EmotionAudio(audio_path)
emotions = emotion_audio.get_audio_emotion()

print(emotions)
```

##
## Ejemplo de Uso con ROBOBO:
### Este ejemplo hace uso de las librerias de video y audio de ROBOBO (robobo-python-video-stream , robobo-python-audio-stream). 
### La idea de este ejemplo es tomar una imagen y capturar el audio, para posterior mente hacer una prediccion de la emocion obtenida de la imagen y el audio capturados.
### Al ejecutar este ejemplo lo ROBOBO comenzara a reproducior en streaming de video lo que captura por su camara frontal, y va a esperar por que la tecla 'r' sea presionada para capturar una imagen. Automaticamente capture la imagen se detiene el streaming de video y conecta el streaming de audio para capturar el audio. Aqui va a esperar por la tecla 's' para detener la captura de audio y comenzar con el procesamiento multimodal para la prediccion de la emoción. 

```python
import datetime
import os
import cv2
import pyaudio
import wave
import keyboard
from robobo_emotion import MultimodalEmotion
from robobopy.Robobo import Robobo
from robobopy_videostream.RoboboVideo import RoboboVideo
from robobopy_audiostream.RoboboAudio import RoboboAudio

def create_capture_folder(base_path):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    folder_name = os.path.join(base_path, f"Captura{timestamp}")
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def save_frame(videoStream, folder_name):
    frame = videoStream.getImage()
    img_path = os.path.join(folder_name, "imagen.jpg")
    cv2.imwrite(img_path, frame)
    return img_path

def record_audio(audioStream, folder_name):
    audio_path = os.path.join(folder_name, "audio.wav")
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    wf = wave.open(audio_path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)

    print("Start speaking now (press 's' to stop)...")
    while True:
        data = stream.read(1024)
        wf.writeframes(data)
        #if cv2.waitKey(10) & 0xFF == ord('s'):
        if keyboard.is_pressed('s'):  # Verifica si la tecla 's' fue presionada
            print("Recording finished.")
            break
    
    print("closing...")
    stream.stop_stream()
    stream.close()
    audioStream.disconnect()
    p.terminate()
    wf.close()
    return audio_path

def main():
    server_address = '192.168.1.177'
    base_path = r"D:\Master\Tesis\Repositorio\robobo_emotion\examples"
    rob = Robobo(server_address)
    videoStream = RoboboVideo(server_address)
    audioStream = RoboboAudio(server_address)

    rob.connect()
    rob.startStream()
    videoStream.connect()
    
    folder_name = create_capture_folder(base_path)
    img_path = None
    audio_path = None
    
    while True:
        cv2.imshow('Video Feed', videoStream.getImage())
        if cv2.waitKey(10) & 0xFF == ord('r'):
            img_path = save_frame(videoStream, folder_name)
            print("Image captured.")
            break

    cv2.destroyAllWindows()
    rob.stopStream()

    # Record audio after capturing the image
    audioStream.connect()
    rob.startAudioStream()
    audio_path = record_audio(audioStream, folder_name)
    audioStream.disconnect()
    rob.stopAudioStream()
    rob.disconnect()

    # Emotional analysis
    if img_path and audio_path:
        analizador = MultimodalEmotion(img_path, audio_path)
        print("Fusión de emociones:", analizador.fusion_emotion)
        print("Emoción predominante:", analizador.predominant_emotion)
        print("Combinacion de emociones:", analizador.emociones_agrupadas)

    print("Program has finished executing.")

if __name__ == "__main__":
    main()

```
