import RPi.GPIO as GPIO
from time import sleep
import sys
import math


class Stepper():

    # Direction pin from controller
    DIR = 38
    # Step pin from controller
    STEP = 36
    # 0/1 used to signify clockwise or counterclockwise.
    CW = 1
    CCW = 0

    def __init__(self):
        self

    def initiateStepper(self):
        # Setup pin layout on PI
        GPIO.setmode(GPIO.BOARD)

        # Establish Pins in software
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.setup(self.STEP, GPIO.OUT)

        # Set the first direction you want it to spin
        GPIO.output(self.DIR, self.CW)

    def AngleRotate(self, x, y):
        angle = math.atan((y - 60) / x)
        angle = int(angle)
        rot = (angle/1.8)
        rot = int(rot)
        rot = round(rot)
        for i in range(0,rot):
            GPIO.output(self.STEP, True)
            # Allow it to get there.
            # Dictates how fast stepper motor will run
            #Set coil winding to low
            GPIO.output(self.STEP, False)
            sleep(.1)



