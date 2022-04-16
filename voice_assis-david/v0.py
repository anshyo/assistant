import pyttsx3
import os
import datetime

def onstart():
    print('password?')
    say('password?')
    password = input()
    while password != 'password':
        print('password?')
        say('password?')
        password = input()
    else:
        pass

    welcome()

    say("write 'y' to open help file")
    help = input('write \'y\' to open help file: ').lower()
    if help == 'y':
        os.system('mousepad voice_assis-david/help')
    else:
        pass

def say(sentence):
    voice = pyttsx3.init()
    voice.say(sentence)
    voice.runAndWait()

def welcome():
    time = int(datetime.datetime.now().hour)
    if time>0 and time<12:
        print('good morning sir')
        say('good morning sir')
    elif time>12 and time<16:
        print('good afternoon sir')
        say('good afternoon sir')
    elif time>16 and time<0:
        print('good evening sir')
        say('good evening sir')
    print('you should go to sleep sir, thats late night')
    say('you should go to sleep sir, thats late night')

def operation_activator():
    print('how can i help you?')
    say('how can i help you?')
    operation_name = input("keyword: ").lower()
    if operation_name == "files":
        open_any_file()
    elif operation_name == "entertain" or "et" :
        print('music or movie?')
        say('music or movie?')
        answer = input().lower
        if answer == "mus":
            play_music()

    else:
        print('wrong keyword')
        say('wrong keyword')
        operation_activator()

def play_music():

    def what_to_play():
        answer = input()
        if answer == "on":
            os.system('spotify')
        elif answer == "off":
            os.system("vlc /home/ansh/Music/")
        else:
            print('error')
            say('error')
            what_to_play()

    print('online(on) or offline(off) ')
    say('online or offline ')
    what_to_play()


def play_movie():
    say('a')

def open_any_file():
    say('coming soon')

if __name__ == "__main__":
    onstart()
    welcome()
    operation_activator()