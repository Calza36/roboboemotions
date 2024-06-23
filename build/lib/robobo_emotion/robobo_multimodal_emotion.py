from deepface import DeepFace
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

class MultimodalEmotion:
    def __init__(self, image_path, audio_path):
        self.image_path = image_path
        self.audio_path = audio_path
        fusion_emotion_results = self.get_fusionemotion()
        self.fusion_emotion = fusion_emotion_results[0]
        self.predominant_emotion = fusion_emotion_results[1]
        self.emociones_agrupadas = fusion_emotion_results[2]

    def get_image_emotion(self):    
        result = DeepFace.analyze(self.image_path, actions=['emotion'], enforce_detection=True)
        img_emotion = result[0]['emotion']
        return img_emotion
    

    def get_audio_emotion(self):
        inference_pipeline = pipeline(
            task=Tasks.emotion_recognition,
            model="iic/emotion2vec_base_finetuned")  # Alternative: iic/emotion2vec_plus_seed, iic/emotion2vec_plus_base, iic/emotion2vec_plus_large and iic/emotion2vec_base_finetuned
        
        audio_emotion_proc = inference_pipeline(self.audio_path, output_dir="./outputs", granularity="utterance", extract_embedding=False)
        audio_emotion_scores= audio_emotion_proc[0]['scores']
        new_audio_emotion = audio_emotion_scores.copy() #Audio con 9 Emociones. Juntamos Neutral con Other y con Unknown

        # Sumar los valores de las posiciones 4, 5 y 8
        sum_value = audio_emotion_scores[4] + audio_emotion_scores[5] + audio_emotion_scores[8]

        # Insertar el valor sumado en la posición 4
        new_audio_emotion[4] = sum_value

        # Eliminar las posiciones 5 y 8 (ajustadas después de la inserción)
        del new_audio_emotion[5]  # Elimina la posición original 5
        del new_audio_emotion[7]  # Ajusta y elimina la posición original 8
        
        #Moviendo la posición 4 al final para que coincida con la posicion de Deepface. 
        # Extraer el valor en la posición 4
        valor = new_audio_emotion[4]

        # Eliminar el valor en la posición 4 del array
        del new_audio_emotion[4]

        # Añadir el valor extraído al final del array 
        new_audio_emotion.append(valor)

        # Multiplicar por 100 los valores del array para estar en la misma base que Deepface
        new_audio_emotion = [x * 100 for x in new_audio_emotion]
        
        # Claves para el diccionario
        claves = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        
        # Convertir la lista de valores en un diccionario con las claves dadas
        diccionario_emociones = dict(zip(claves, new_audio_emotion))


        audio_emotion = diccionario_emociones
        return audio_emotion
    
    def get_fusionemotion(self):
        img_emotion = self.get_image_emotion()
        audio_emotion = self.get_audio_emotion()
        
        fusion_emotion = {clave: img_emotion[clave] * 0.6 + audio_emotion[clave] * 0.4 for clave in img_emotion}

        # Encontrar el máximo valor y su clave correspondiente
        max_key = max(fusion_emotion, key=fusion_emotion.get)  # Obtiene la clave con el valor máximo
        max_value = fusion_emotion[max_key]     


        emociones_agrupadas = {'happy': 0, 'negativo': 0, 'neutral': 0, 'surprise': 0}

        # Agrupar emociones bajo "Negativo"
        for emocion, valor in fusion_emotion.items():
            if emocion in ['angry', 'disgust', 'fear', 'sad']:
                emociones_agrupadas['negativo'] += valor
            else:
                emociones_agrupadas[emocion] = valor

        # Encontrar la emoción predominante

        if max_key in ['angry', 'disgust', 'fear', 'sad']:
            max_key = 'negativo'

        predominant_emotion = {max_key: max_value}
        


        #fusion_emotion = self.fusion(img_emotion, audio_emotion)

        return fusion_emotion, predominant_emotion, emociones_agrupadas
    
    


    def get_image_path(self):
        return self.image_path
    
    def get_audio_path(self):
        return self.audio_path
    
    



