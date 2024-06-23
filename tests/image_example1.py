from robobo_emotion import EmotionImage

image_path = "src\Anger.jpg"
emotion_image = EmotionImage(image_path)
emotion = emotion_image.get_emotion()

print(emotion)

