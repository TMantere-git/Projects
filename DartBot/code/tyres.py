import RPi.GPIO as gpio
import time

MO1 = 
MO2 = 
MV1 = 
MV2 =
ENO =
ENV =


gpio.setmode(gpio.BCM)

gpio.setup(MO1, gpio.OUT)
gpio.setup(MO2, gpio.OUT)
gpio.setup(MV1, gpio.OUT)
gpio.setup(MV2, gpio.OUT)

pwm1=GPIO.PWM(EN0,100)
pwm2=GPIO.PWM(ENV,100)
pwm1.start(50)
pwm2.start(50)

def eteen():
    gpio.output(MO1, True)
    gpio.output(MO2, False) 
    gpio.output(MV1, True) 
    gpio.output(MV2, False) 
    gpio.output(ENO, True)
    gpio.output(ENV, True)
    
 def taakse():
    gpio.output(MO1, False)
    gpio.output(MO2, True) 
    gpio.output(MV1, False) 
    gpio.output(MV2, True) 
    gpio.output(ENO, True)
    gpio.output(ENV, True)


def vasemmalle():
    gpio.output(MO1, True)
    gpio.output(MO2, False)
    gpio.output(MV1, False) 
    gpio.output(MV2, True) 
    gpio.output(ENO, True)
    gpio.output(ENV, True)
    

def oikealle():
    gpio.output(MO1, False) 
    gpio.output(MO2, True) 
    gpio.output(MV1, True)
    gpio.output(MV2, False)
    gpio.output(ENO, True)
    gpio.output(ENV, True)
   

def carTurnO():
    #oikealle 90 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnV():
    #vasemmalle 90 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
def carTurnO120():
    #oikealle 20 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnO140():
    #oikealle 40 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnO160():
    #oikealle 60 astetta kerrallaan
    oikealle()
    sleep(" ")
    
def carTurnV20():
    #vasemmalle 20 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
def carTurnV40():
    #vasemmalle 40 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
 def carTurnV60():
    #vasemmalle 60 astetta kerrallaan
    vasemmalle()
    sleep(" ")
    
   
   
  
    
