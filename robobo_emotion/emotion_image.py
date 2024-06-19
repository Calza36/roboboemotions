from deepface import DeepFace

class EmotionImage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.emotion = self.get_emotion()

    def get_emotion(self):
        #result = DeepFace.analyze(self.image_path)
        #emotion = result[0]['dominant_emotion']
        result = DeepFace.analyze(self.image_path, actions=['emotion'])
        emotion = result[0]['dominant_emotion']
        return emotion

    def get_image_path(self):
        return self.image_path



