import datetime
import os
from time import sleep
from robobo_multimodal_emotion import MultimodalEmotion
from robobopy.Robobo import Robobo
from robobopy_videostream.RoboboVideo import RoboboVideo
from robobopy_audiostream.RoboboAudio import RoboboAudio
from robobopy_audiostream.Exceptions import ClosedConnection
import cv2
import pyaudio
import wave

p = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

server_address = '192.168.1.177'
rob = Robobo(server_address)

#The IP must be that shown in the Robobo app
videoStream = RoboboVideo(server_address)
audioStream = RoboboAudio(server_address)


base_path = r"D:\Master\Tesis\Repositorio\robobo_emotion\examples"

def create_capture_folder():
    """Crea una nueva carpeta para guardar captura de imagen y audio."""
    # Incluir milisegundos en el timestamp para nombres de archivo únicos
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    folder_name = os.path.join(base_path, f"Captura{timestamp}")
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def save_frame(frame, folder_name):
    """Guarda el frame actual en la carpeta designada."""
    img_path = f"{folder_name}/imagen.jpg"
    cv2.imwrite(img_path, frame)
    return img_path

def save_audio(folder_name, p):
    audio_path = f"{folder_name}/audio.wav"
    wf = wave.open(audio_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    return audio_path, wf

def main():
    print("Starting test app")
    #Connect to the robot and start the video and audio stream
    rob.connect()
    rob.startStream()
    videoStream.connect()
    
    rob.startAudioStream()
    audioStream.connect()

    while True:
        cv2_image = videoStream.getImage()
        cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
        cv2.imshow('imagen', cv2_image)
        key = cv2.waitKey(1)

        if key == ord('r'):
            folder_name = create_capture_folder()
            img_path = save_frame(cv2_image, folder_name)

            # wait 1.5 seconds to capture audio
            sleep(1)
            #Audio streaming starting
            audio_path, wf = save_audio(folder_name, p)
            stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
            while audioStream.isConnected():
                try:
                    data = audioStream.getAudioWithMetadata()
                    if data is not None:
                        # Process audio data as needed
                        timestamp, sync, audio_data = data
                        #print(f"Timestamp: {timestamp}, Sync: {sync}, Audio Data Length: {len(audio_data)}")
                        stream.write(audio_data)
                        wf.writeframes(audio_data)
                        stopkey = cv2.waitKey(1)
                        if stopkey == ord('s'):
                            #stream.stop_stream()
                            #stream.close()
                            #wf.close()
                            #audioStream.disconnect()
                            #rob.stopAudioStream()
                            break 
                except ClosedConnection:
                    break
                except KeyboardInterrupt:
                    break
            stream.stop_stream()
            stream.close()
            # Cierra el archivo WAV después de grabar
            wf.close() # Ahora el audio está guardado en audio_path
           
            audioStream.disconnect()
            rob.stopAudioStream()

            
        # Exit loop if 'q' key is pressed
        if key == ord('q'):
            break

    # si img_path y audio_path existen, se puede analizar la emoción
    if img_path and audio_path:
        # Detectar emocion con MultimodalEmotion
        analizador = MultimodalEmotion(img_path, audio_path)
        print("Fusión de emociones:", analizador.fusion_emotion)
        print("Emoción predominante:", analizador.predominant_emotion)
        print("Emociones agrupadas:", analizador.emociones_agrupadas)

    
    # Release resources
    cv2.destroyAllWindows()
    rob.stopStream()
    rob.disconnect()
    

if __name__ == "__main__":
    main()







