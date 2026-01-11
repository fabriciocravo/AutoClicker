from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener
import time
import pygame

mouse = MouseController()
clicking = False
running = True

pygame.mixer.init()

# Your downloaded sound file
sound_file = "for-p-453681.mp3"

alarm_sound = pygame.mixer.Sound(sound_file)


def on_press(key):
    global clicking, running

    if key == Key.shift or key == Key.shift_r:
        clicking = not clicking
        print("Clicking ON" if clicking else "Clicking OFF")

        if clicking:
            alarm_sound.play(loops=-1)
        else:
            alarm_sound.stop()

    if hasattr(key, 'char') and key.char == '1':
        running = False
        alarm_sound.stop()
        pygame.mixer.quit()
        return False


listener = Listener(on_press=on_press)
listener.start()

print("Autoclicker ready!")
print("Press SHIFT to toggle (music plays when active)")
print("Press 1 to stop")

while running:
    if clicking:
        mouse.press(Button.left)
        time.sleep(0.01)
        mouse.release(Button.left)
        time.sleep(0.01)
    else:
        time.sleep(0.1)

alarm_sound.stop()
pygame.mixer.quit()
print("Autoclicker stopped")