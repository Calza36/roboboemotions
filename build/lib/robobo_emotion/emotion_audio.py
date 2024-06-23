from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class EmotionAudio:
    def __init__(self, audio_path, model="iic/emotion2vec_base_finetuned"):
        # Guarda el path del audio
        self.audio_path = audio_path
        
        # Inicializa el pipeline de inferencia con el modelo especificado
        self.model = model

    def get_audio_emotion(self):
        # Configura el pipeline de inferencia con el modelo especificado
        inference_pipeline = pipeline(
            task=Tasks.emotion_recognition,
            model=self.model
        )

        # Realiza la inferencia sobre el audio proporcionado
        audio_emotion_proc = inference_pipeline(self.audio_path, output_dir="./outputs", granularity="utterance", extract_embedding=False)
        audio_emotion_scores = audio_emotion_proc[0]['scores']

        # Copia los scores para modificarlos
        new_audio_emotion = audio_emotion_scores.copy()

        # Sumar los valores de las posiciones 4, 5 y 8 y actualizar la posición 4
        sum_value = audio_emotion_scores[4] + audio_emotion_scores[5] + audio_emotion_scores[8]
        new_audio_emotion[4] = sum_value

        # Eliminar las posiciones 5 y 8 (ajustadas después de la inserción)
        del new_audio_emotion[5]  # Elimina la posición original 5
        del new_audio_emotion[7]  # Ajusta y elimina la posición original 8
        
        # Extraer el valor en la posición 4, eliminarlo del array y añadirlo al final
        valor = new_audio_emotion.pop(4)
        new_audio_emotion.append(valor)

        # Multiplicar por 100 los valores del array para estar en la misma base que Deepface
        new_audio_emotion = [x * 100 for x in new_audio_emotion]

        # Claves para el diccionario de emociones
        claves = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

        # Convertir la lista de valores en un diccionario con las claves dadas
        diccionario_emociones = dict(zip(claves, new_audio_emotion))

        return diccionario_emociones