#import tyres as ty                  # Includes tyre movements
#import camera as cam                # Includes camera functions
import solenoid as sol              # Function for solenoid burst, "trigger"
import FireAtWill as fire           # Launch function
import LocknLoad as load            # Load function
import RPi.GPIO as gpio
#import stepper_motor as step


from time import sleep

camOK = False                       # setup booleans, always False at start
motor = False
servos = False

dartrdy = False

DartCount = 1 
                      # Dart counter, in this solution max dart count is 3

def main_fire():
    global DartCount                             # Shooting happens only if camera and motors are ok
    global dartrdy
    if DartCount < 4:              # and Dart count is lower than 4, meaning 1, 2, or 3

        if dartrdy == False:
            dartrdy = True
            #load.LocknLoad(dartrdy)
            print("reload")
            
        if dartrdy == True:
            dartrdy = False
            fire.FireAtWill()
            DartCount = DartCount + 1
            sleep(0.5)
    #else:                          # if DartCount would be 4, or anything else shooting won't happen
        #ShutDown()


def ShutDown():                         # After successfully fired 3 darts
    # DOES WHATEVER DARTBOT DOES
    while(1):
        print("DartCount is ", DartCount)
        print("LOPPU")
        sleep(1000000)


