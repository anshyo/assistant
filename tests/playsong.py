from pygame import *
mixer.init()
mixer.music.load('/home/ansh/Music/Alan-Walker-Faded.mp3')
mixer.music.play()

while True:
      
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
      
    if query == 'p':
  
        # Pausing the music
        mixer.music.pause()     
    elif query == 'r':
  
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
  
        # Stop the mixer
        mixer.music.stop()
        break