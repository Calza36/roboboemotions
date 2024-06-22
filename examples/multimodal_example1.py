from robobo_multimodal_emotion import MultimodalEmotion

image_path = r"D:\Master\Tesis\Repositorio\robobo_emotion\examples\Anger.jpg"
audio_path = r"D:\Master\Tesis\Repositorio\robobo_emotion\examples\YAF_match_angry.wav"

# Crear una instancia de MultimodalEmotion
analizador = MultimodalEmotion(image_path, audio_path)

# Acceder a los resultados
print("Fusión de emociones:", analizador.fusion_emotion)
print("Emoción predominante:", analizador.predominant_emotion)
print("Emociones agrupadas:", analizador.emociones_agrupadas)
