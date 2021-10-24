from pynput.keyboard import Key, Listener

directions = ["w", "a", "s", "d"] # forward, left, backward, right
speeds = [0, 1, 2, 3, 4, 5] # motor speeds

direction = ""
speed = 0

def on_press(key):
    if str(key.char) in directions:
        direction = str(key)
        print(direction)
    elif int(key.char) in speeds:
        speed = key
        print(speed)
    else:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()