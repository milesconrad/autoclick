from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
from threading import Thread
from time import sleep

mouse = Controller()
active = False
lastKey = None

def on_press(pressedKey):
    global active
    global lastKey
    
    # if you try to call pressedKey.char when pressedKey is a key object, then
    # it throws an AttributeError and this thread closes
    if not isinstance(pressedKey, Key):
        if pressedKey.char == ']':
            if not isinstance(lastKey, Key):
                if lastKey.char == '[':
                    active = not active

    lastKey = pressedKey
    
def clicker():
    while True:
        if active:
            mouse.click(Button.left)
            sleep(0.005)

clickerThread = Thread(target=clicker)
listenerThread = Listener(on_press=on_press)

listenerThread.start()
clickerThread.start()

listenerThread.join()
clickerThread.join()