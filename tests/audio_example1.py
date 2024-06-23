from robobo_emotion import EmotionAudio

audio_path = "examples\YAF_match_angry.wav"
emotion_audio = EmotionAudio(audio_path)
emotions = emotion_audio.get_audio_emotion()

print(emotions)