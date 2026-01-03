from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener
import time
import random

mouse = MouseController()
clicking = False
running = True


def on_press(key):
    global clicking, running

    if key == Key.shift or key == Key.shift_r:
        clicking = not clicking
        print("Clicking ON" if clicking else "Clicking OFF")

    if hasattr(key, 'char') and key.char == '1':
        running = False
        return False


listener = Listener(on_press=on_press)
listener.start()

print("Autoclicker ready!")
print("Press SHIFT to toggle clicking")
print("Press 1 to stop")

while running:
    if clicking:
        mouse.press(Button.left)
        time.sleep(0.05)
        mouse.release(Button.left)
        time.sleep(0.05)
    else:
        time.sleep(0.1)

print("Autoclicker stopped")