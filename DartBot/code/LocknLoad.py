import RPi.GPIO as gpio
from time import sleep
#import stepper_motor as step

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)


gpio.setup(22, gpio.OUT)                 # Stepper motor pins
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(26, gpio.OUT)

def LocknLoad(dartrdy):                        # Dart is laoded to the chamber ready to shoot
        
#       step.steppermotor()
        print("reload")
