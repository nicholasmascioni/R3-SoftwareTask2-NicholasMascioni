from pynput.keyboard import Key, Listener

directions = ["w", "a", "s", "d"] # forward, left, backward, right
speeds = [0, 1, 2, 3, 4, 5] # motor speeds

direction = ""
speed = 0

def on_press(key):
    if key.char in directions or int(key.char) in speeds:
        print(key)

with Listener(on_press=on_press) as listener:
    listener.join()