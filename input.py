from pynput import keyboard

directions = ["w", "a", "s", "d"] # forward, left, backward, right
speeds = [0, 1, 2, 3, 4, 5] # motor speeds

direction = ""
speed = 0

def on_press(key):
    try:
        if key in directions:
            print("Key {0} pressed".format(key.char))
            direction = key
        elif key in speeds:
            print("Key {0} pressed".format(key.char))
            speed = key
    except AttributeError:
        print("special Key {0} pressed".format(key))

def on_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

keyboard.Listener()

while True:
    print(direction)
    print(speed)