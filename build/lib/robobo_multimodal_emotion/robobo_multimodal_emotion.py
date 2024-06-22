from deepface import DeepFace

class MultimodalEmotion:
    def __init__(self, image_path, audio_path):
        self.image_path = image_path
        self.audio_path = audio_path
        self.multimodalemotion = self.get_fusionemotion()

    def get_image_emotion(self):    
        result = DeepFace.analyze(self.image_path)
        img_emotion = result[0]
        return img_emotion
    
    def get_audio_emotion(self):


        return audio_emotion
    
    def get_fusionemotion(self):
        img_emotion = self.get_image_emotion()
        audio_emotion = self.get_audio_emotion()
        fusion_emotion = self.fusion(img_emotion, audio_emotion)
        return fusion_emotion
    
    def fusion(self, img_emotion, audio_emotion):
        

    def get_image_path(self):
        return self.image_path
    
    def get_audio_path(self):
        return self.audio_path
    
    



