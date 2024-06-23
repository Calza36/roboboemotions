from robobo_emotion import MultimodalEmotion

image_path = "src\Anger.jpg"
audio_path = "src\YAF_match_angry.wav"

# Crear una instancia de MultimodalEmotion
analizador = MultimodalEmotion(image_path, audio_path)

# Acceder a los resultados
print("Fusión de emociones:", analizador.fusion_emotion)
print("Emoción predominante:", analizador.predominant_emotion)
print("Combinacion de emociones:", analizador.emociones_agrupadas)
