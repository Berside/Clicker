import time
import mouse 
import keyboard

inClick = False

def set_click():
    global inClick
    if inClick:
        inClick = False
        print("Disabled!")
    else:
        inClick = True
        print("Аctived!")

keyboard.add_hotkey('Z', set_click)

while True:
    if inClick:
        mouse.double_click(button = "left")
        time.sleep(0.1)