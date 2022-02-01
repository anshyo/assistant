import webbrowser
import time
import subprocess
print("             ______________                                ")
print("            /              \                               ")
print("           /   $$      $$   \                _____         ")
print("          |         A        |       |   |  |      \  /    ")
print("          |                  |       |---|  |-----  \/     ")
print("          |    \________/    |       |   |  |_____  ||     ")
print("           \                /                       ||     ")
print("            \______________/                               ")
print("")
print("________________________________________________________________________________________________________________")
print("what do you want to open :")
print("1. \"l\" for link")
print("2. \"a\" for apps")
a=input("write \"l\" or \"a\": \n")
print("________________________________________________________________________________________________________________")



def open_apps():
    print('what do you wanna open? just type:')
    print("1. \"c\" for calculator")
    print("2. \"note\" for notepad")
    print("3. \"cmd\" for cmd")
    b=input('write here:')
    if b=="c":
        subprocess.call("calc.exe")
    elif b=="note":
        subprocess.call("notepad.exe")
    elif b=="cmd":
        subprocess.call("cmd.exe")
    else:
        print("invalid")

def open_links():
        print("________________________________________________________________________________________________________________")
        print("What do you wanna open in browser? just type:")
        print("1. \"g\" for google")
        print("2. \"y\" for Youtube")
        print("3. \"w\" for Whatsapp")
        print("4. \"s\" for Spotify")
        print("5. \"vc\" for VScode")
        print("5. \"cm\" for write your own url")
        print("________________________________________________________________________________________________________________")
        b=input("write here:")
        if b=="g":
            webbrowser.open("https://www.google.co.in/")
        elif b=="y":
            webbrowser.open("https://www.youtube.com/")
        elif b=="w":
            webbrowser.open("https://web.whatsapp.com/")
        elif b=="s":
            webbrowser.open("https://open.spotify.com/?utm_source=pwa_install")
        elif b=="vc":
            webbrowser.open("https://vscode.dev/")
        elif b=="cm":
            s=input()
            webbrowser.open(s)
        else:
            print ("Invalid")  

def cycle():
    if a=="l":
        open_links()      
    if a=="a":
        open_apps()
    else:
        print("Invalid")

cycle()
print("________________________________________________________________________________________________________________")
print('now, do you wanna open new app or link?')
t=input(" if yes,type \"y\" and if no, type \"n\":")
print("________________________________________________________________________________________________________________")
while t!="n" or t=="y":
    cycle()
    continue
else:
    print("                      _____                      ")
    print("  |   |   /\  \    / |             /\            ")
    print("  |---|  /__\  \  /  |----        /__\           ")
    print("  |   | /    \  \/   |_____      /    \          ")
    print("                                                 ")
    print("        _______    __   ____       __            ")
    print("  |\  |    |      /    |          |  \   /\  \  /")
    print("  | \ |    |     |     |---       |   | /__\  \/ ")
    print("  |  \| ___|___   \__  |_____     |__/ /    \ || ")
    print("                                              || ")
    time.sleep(5)
    quit    
