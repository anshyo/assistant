from email.mime import audio
import speech_recognition as sr
import pyttsx3

david=pyttsx3.init()
david.setProperty('rate', 150)

def say(line):
    david.say(line)
    david.runAndWait()
    david.stop()

def main():
 
    r = sr.Recognizer()
 
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
 
        say("Please say something")
 
        audio = r.listen(source)

 
        say("Recognizing Now .... ")
 
 
        # recognize speech using google
 
        try:
            say("You have said \n" + r.recognize_google(audio , language='en-in'))
            print("You have said \n" + r.recognize_google(audio))
            say("Audio Recorded Successfully \n ")
 
 
        except Exception as e:
            say("Error :  " + str(e))
 
 
 
 
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
 
 
if __name__ == "__main__":
    main()