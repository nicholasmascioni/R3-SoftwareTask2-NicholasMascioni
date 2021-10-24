# R3-SoftwareTask2-NicholasMascioni

For this project I was tasked with creating two programs: one to act as a client and one to act as a server.

## The Client Program
The goal of the client program was to monitor keyboard inputs to simulate controlling a rover. I used the pynput library to assist in monitoring the keyboard to check if specific keys were pressed.

I began by creating two lists and variables. The *directions* list stores all the possible directional inputs from the keyboard. (w, a, s, d for forward, left, backward, and right respectively) The *speeds* list stores all the possible speeds the motors can be run at. (0 being off and 5 being the fastest) The *direction* and *speed* variables are there to store the respective value that has been inputted. 
```
directions = ["w", "a", "s", "d"] 
speeds = [0, 1, 2, 3, 4, 5]

direction = ""
speed = 0
```

Next, I used the pynput library to monitor which keys are being pressed. The *onPress()* function takes *key* as an argument, which is the key being pressed. If the key is in *directions*, (if the key is either w, a, s, or d) the key is stored in *direction*. If the key is in *speeds*, (if the key is either 0, 1, 2, 3, 4, or 5) the key is stored in *speed*. 
```
def on_press(key):
    if str(key.char) in directions:
        direction = str(key)
        print(direction)
    elif int(key.char) in speeds:
        speed = key
        print(speed)
    else:
        pass
```

The next line uses the *Listener* function from the pynput library to monitor the keyboard for inputs.
```
with Listener(on_press=on_press) as listener:
    listener.join()
```

## The Server Program
The goal of the server program was to act as a rover, receiving inputs from the client program in order to control its direction and the speed of its motors. The simulated rover was supposed to have **differential steering**, meaning forward and backward would have all motors running in the respective direction, left would have the left motors moving backwards while the right motors move forward, and right would have the left motors moving forward while the right motors move backward. This is also referred to as "tank steering" ocassionally. 

The varying motor speeds are supposed to represent **PWM** (pulse-width modulation) signals, which are digital signals used to simulate analog signals. An example of this is dimming and brightening an LED.

The client and server programs were meant to communicate with eachother via the socket module, allowing for data to be sent between the programs. 

The goal was to send the *direction* and *speed* variables to the server program and output the correct speeds and directions for each motor with the server program once it has received the input data.

Unfortunately I did not have time to learn how to do this, as I've been very busy with schoolwork, especially since midterms are approaching once again. I began to follow a tutorial from realpython.com on socket programming in python, but was not able to finish it before the deadline. 

I would like to finish this project someday, when I have more time, as I found it very interesting, and I feel the skills learned here could be implemented in other ways in different applications. 