# USAGE 
# python3 pan_tilt_tracking.py --cascade haarcascade_frontalface_default.xml 
 
# import necessary packages 
from multiprocessing import Manager 
from multiprocessing import Process 
from imutils.video import VideoStream 
from pyimagesearch.objcenter import ObjCenter 
from pyimagesearch.pid import PID 
from time import sleep
import Robo as rob
#import DistanceCalculation as DC
import argparse, signal, time, sys, cv2 
 
# Define the range for the motors, check more appropriate values later 
servoRange = (-65, 65, -65, -20) 

import RPi.GPIO as GPIO
import pigpio
pi = pigpio.pi() 
s1 = 3 #upper servo
s2 = 2 #lower servo
us_min = 1000
us_max = 2000 
panAngle = 0
tltAngle = -25
turn, PA = 0
 
def setServoAngle(servo, angle): 
        angle += 65
        servo_range = us_max - us_min
        us = (servo_range / 130.0) * angle
        turn = us_min + int(us)
        pi.set_servo_pulsewidth(servo, turn)

# function to handle keyboard interrupt 
def signal_handler(sig, frame): 
    # print a status message
    print("[INFO] You pressed `ctrl + c`! Exiting...")
 
    # Disable the servos. These are assigned to pins 3 (SDA) and 5 (SDL) 
    #pth.servo_enable(1, False) 
    #pth.servo_enable(2, False) 
 
    # exit 
    sys.exit() 
 
def obj_center(args, objX, objY, centerX, centerY): 
    # signal trap to handle keyboard interrupt 
    signal.signal(signal.SIGINT, signal_handler) 
 
    # start the video stream and wait for the camera to warm up 
    vs = VideoStream(usePiCamera=True).start() 
    time.sleep(2.0) 

    # initialize the object center finder 
    obj = ObjCenter(args["cascade"]) 
    

    # loop indefinitely 
    while True: 
        # grab the frame from the threaded video stream and flip it 
        # vertically (since our camera was upside down) 
        frame = vs.read() 
        frame = cv2.flip(frame, 0) 
 
        # calculate the center of the frame as this is where we will 
        # try to keep the object 
        (H, W) = frame.shape[:2] 
        centerX.value = W // 2 
        centerY.value = H // 2 

        # find the object's location 
        objectLoc = obj.update(frame, (centerX.value, centerY.value)) 
        ((objX.value, objY.value), rect) = objectLoc 

        # extract the bounding box and draw it 
        if rect is not None: 
            (x, y, w, h) = rect 
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
            print("w, h, x, y:" , w, h, x, y)
            dRat = 36/36 
            Rat = w/h 
            if Rat == dRat and x > 138 and x < 145 and y > 97 and y < 105: 
                #DC.DistanceCalculation(w, dX) 
                rob.main_fire()
                
        # display the frame to the screen 
        cv2.imshow("Pan-Tilt Face Tracking", frame) 
        cv2.waitKey(1) 
 
def pid_process(output, p, i, d, objCoord, centerCoord): 
    # signal trap to handle keyboard interrupt 
    signal.signal(signal.SIGINT, signal_handler)
    # create a PID and initialize it 
    pid = PID(p.value, i.value, d.value) 
    pid.initialize() 

    # loop indefinitely 
    while True: 
        # calculate the error
        error = centerCoord.value - objCoord.value

        # update the value 
        output.value = pid.update(error)
 
def in_range(val, start, end): 
    # determine the input vale is in the supplied range 
    return (val >= start and val <= end) 
 
def set_servos(pan, tlt):
    global panAngle, tltAngle
    # signal trap to handle keyboard interrupt 
    signal.signal(signal.SIGINT, signal_handler) 

    # loop indefinitely 
    while True: 
        # the pan and tilt angles are reversed
        panAngle = -1*pan.value
        tltAngle = -1*tlt.value
 
        # if the pan angle is within the range, pan 
        if in_range(panAngle, servoRange[0], servoRange[1]):
            setServoAngle(s2, panAngle) 
 
        # if the tilt angle is within the range, tilt 
        if in_range(tltAngle, servoRange[2], servoRange[3]):
            setServoAngle(s1, tltAngle) 
 
# check to see if this is the main body of execution 
while __name__ == "__main__": 
    # construct the argument parser and parse the arguments 
    ap = argparse.ArgumentParser() 
    ap.add_argument("-c", "--cascade", type=str, required=True, 
        help="/home/pi/Desktop/DartBot-master/pan_tilt_tracking/haarcascade_frontalface_default.xml") 
    args = vars(ap.parse_args()) 
    setServoAngle(s1, tltAngle)
    # start a manager for managing process-safe variables
    with Manager() as manager:
        try:
            # Enable the servos, might be no need for this 
            #pth.servo_enable(1, True) 
            #pth.servo_enable(2, True) 
     
            # set integer values for the object center (x, y)-coordinates 
            centerX = manager.Value("i", 0) 
            centerY = manager.Value("i", 0) 
     
            # set integer values for the object's (x, y)-coordinates 
            objX = manager.Value("i", 0) 
            objY = manager.Value("i", 0) 
     
            # pan and tilt values will be managed by independed PIDs 
            pan = manager.Value("i", 0) 
            tlt = manager.Value("i", -40) 
     
            # set PID values for panning 
            panP = manager.Value("f", 0.09) 
            panI = manager.Value("f", 0.08) 
            panD = manager.Value("f", 0.002) 
     
            # set PID values for tilting 
            tiltP = manager.Value("f", 0.11) 
            tiltI = manager.Value("f", 0.10) 
            tiltD = manager.Value("f", 0.002) 
     
            # we have 4 independent processes 
            # 1. objectCenter  - finds/localizes the object 
            # 2. panning       - PID control loop determines panning angle 
            # 3. tilting       - PID control loop determines tilting angle 
            # 4. setServos     - drives the servos to proper angles based 
            #                    on PID feedback to keep object in center 
            processObjectCenter = Process(target=obj_center, 
                args=(args, objX, objY, centerX, centerY)) 
            processPanning = Process(target=pid_process, 
                args=(pan, panP, panI, panD, objX, centerX)) 
            processTilting = Process(target=pid_process, 
                args=(tlt, tiltP, tiltI, tiltD, objY, centerY)) 
            processSetServos = Process(target=set_servos, args=(pan, tlt)) 
     
            # start all 4 processes 
            processObjectCenter.start() 
            processPanning.start() 
            processTilting.start() 
            processSetServos.start() 
     
            # join all 4 processes 
            processObjectCenter.join() 
            processPanning.join() 
            processTilting.join() 
            processSetServos.join() 
     
            # Disable the servos. Normal code, might not need to disable 
            #pth.servo_enable(1, False) 
            #pth.servo_enable(2, False) '
        except KeyboardInterrupt:
            break

pi.stop()
GPIO.cleanup()
