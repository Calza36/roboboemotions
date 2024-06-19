from robobo_emotion import EmotionImage

image_path = "robobo_emotion\examples\Anger.jpg"
emotion_image = EmotionImage(image_path)
emotion = emotion_image.get_emotion()
print(emotion)

