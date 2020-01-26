import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)


def solenoidburst():
    
    gpio.output(11, True)      # solenoid is given a burst to send the dart in motion
            
    sleep(1)
    
    gpio.output(11, False)
    
