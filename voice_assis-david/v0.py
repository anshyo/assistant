from json.tool import main
from email.mime import audio
import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sp
from pygame import *

david=pyttsx3.init()
david.setProperty('rate', 150)
david.setProperty('volume',7)


def say(line):
    david.say(line)
    david.runAndWait()
    david.stop()

def start():
    time= datetime.datetime.now().hour
    if time>=6 and time<=12:
        say('good morning sir!') 
    elif time>=12 and time<=17:
        say('good afternoon sir!') 
    else:
        say('good evening sir!') 
    say('its david')

 



if __name__=='__main__':
    start()

