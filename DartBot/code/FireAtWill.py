import RPi.GPIO as gpio
import solenoid as sol
from time import sleep
gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)
gpio.setup(13, gpio.OUT)               # Launch motor pin


def FireAtWill():                       # Shooting function
        gpio.output(13, True)
                  
        sleep(1)
        sol.solenoidburst()           # After waiting 5 seconds solenoid burst will fire the dart

        gpio.output(13, False)
