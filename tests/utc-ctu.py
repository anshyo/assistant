import pyttsx3
import speech_recognition as sr

rec=sr.Recognizer()

def say(command):
    engine=pyttsx3.init('sapi15')
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as src:
    rec.adjust_for_ambient_noise(source=2, duration=2)
    audio=rec.listen(src)
    text=rec.recognize_bing(audio)
    text=text.lower()
    say('did you say ' + text )