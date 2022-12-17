import RPi.GPIO as GPIO
from time import sleep
import sys


class Gripper():

    pinGrip = 16

    def __init__(self):
        self

    def runGripper(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinGrip, GPIO.OUT)

        pwm=GPIO.PWM(self.pinGrip, 50)
        pwm.start(0)

    def setAngle(angle, pwm):
        angle = int(angle)
        duty = angle / 18 + 2
        pwm.ChangeDutyCycle(duty) 

    def openGripper(self):
        self.setAngle(0, self.pwm, self.pinGrip)
        sleep(3) 

    def closeGripper(self):
        self.setAngle(140, self.pwm, self.pinGrip)
        sleep(3)