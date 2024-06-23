import datetime
import os
import cv2
import pyaudio
import wave
import keyboard
from robobo_multimodal_emotion import MultimodalEmotion
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
        print("Emociones agrupadas:", analizador.emociones_agrupadas)

    print("Program has finished executing.")

if __name__ == "__main__":
    main()
