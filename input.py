from pynput import keyboard

directions = ["w", "a", "s", "d"] # forward, left, backward, right
speeds = [0, 1, 2, 3, 4, 5] # motor speeds

def on_press(key):
    global direction_input

    try:
        if key.char in directions:
            direction_input = key.char
            return False # Stop listening for inputs
    except AttributeError as ex:
        print(ex)
def on_release(key):
    if key == keyboard.Key.esc:
        return False # Stop listening when esc is pressed

def wait_for_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    if direction_input == "w":
        print("Forward")
    elif direction_input == "s":
        print("Backward")
    elif direction_input == "a":
        print("Left")
    elif direction_input == "d":
        print("Right")
    else:
        print("See ya!")