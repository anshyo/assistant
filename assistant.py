import os
import datetime
from tkinter import mainloop
import pywhatkit
import webbrowser

def onstartup():
    print('hello!')
    print('''
    what do you wanna do?
    1."google" for google search
    2."app" for opening app
    3."link" for opening any link
    ''')

def googleSearch(search):
    pywhatkit.search(search)

def openApp(appname):
    os.system(appname)

def openLink(link):
    webbrowser.open(link)

if __name__=='__main__':
    pasw=input('write password or "e" to exit: ').lower()
    while pasw!='e':
        pasw=input('write password or "e" to exit: ').lower()
        if pasw=='password':
            onstartup()
            work=input('write google/app/link: ').lower()
            if work=='google':
                search=input('what do you wanna search: ').lower()
                googleSearch(search)
                print()
            elif work=='app':
                name=input('name of app: ').lower()
                openApp(name)
                print()
            elif work=='link':
                link=input('write full address: ')
                openLink(link)
                print()
            else:
                print('invalid')
                mainloop()
    else:
        mainloop()
        

    


