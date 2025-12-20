from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, Controller as KeyboardController
import time

mouse = MouseController()
clicking = False
running = True


def on_press(key):
    global clicking, running

    try:
        # Check if shift is pressed
        if key == Key.shift or key == Key.shift_r:
            clicking = not clicking
    except AttributeError:
        pass

    # Stop program when '1' is pressed
    try:
        if hasattr(key, 'char') and key.char == '1':
            running = False
            return False  # Stop listener
    except AttributeError:
        pass


# Start keyboard listener
listener = Listener(on_press=on_press)
listener.start()

print("Autoclicker ready!")
print("Hold SHIFT to click")
print("Press 1 to stop")

# Main clicking loop
while running:
    if clicking:
        mouse.click(Button.left, 1)
        time.sleep(0.0001)  # ~1ms delay = very fast clicking
    else:
        time.sleep(0.001)

print("Autoclicker stopped")