import RPi.GPIO as GPIO 
from time import sleep 



class GPioServo():

    # Initial angles
    theta1 = 40
    theta2 = 65    
    theta3 = 180 

    # Pin locations 
    Pin1a = 3
    Pin1b = 5
    Pin2a = 7
    Pin2b = 11
    Pin3 = 16
    Pin4 = 15 


    # PWM 
    ######## NEED TO ACCOUNT FOR THE NEW CODE STILL ##########
    Pwm1a = None
    Pwm1b = None 
    Pwm2a = None 
    Pwm2b = None 
    Pwm3 = None

    def __init__(self):
        self
        # self.Pin1a = Pin1a
        # self.Pin1b = Pin1b
        # self.Pin2a = Pin2a
        # self.Pin2b = Pin2b
        # self.Pin3 = Pin3

    def start_gpio(self):

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.Pin1a, GPIO.OUT)
        GPIO.setup(self.Pin1b, GPIO.OUT)
        GPIO.setup(self.Pin2a, GPIO.OUT)
        GPIO.setup(self.Pin2b, GPIO.OUT)
        GPIO.setup(self.Pin3, GPIO.OUT)

        self.Pwm1a = GPIO.PWM(self.Pin1a, 50)
        self.Pwm1b = GPIO.PWM(self.Pin1b, 50) 
        self.Pwm2a = GPIO.PWM(self.Pin2a, 50) 
        self.Pwm2b = GPIO.PWM(self.Pin2b, 50)
        self.Pwm3 = GPIO.PWM(self.Pin3, 50)

        self.Pwm1a.start(0)
        self.Pwm1b.start(0)
        self.Pwm2a.start(0)
        self.Pwm2b.start(0)
        self.Pwm3.start(0)

    def setAngle(self, angle, pwm):
        angle = int(angle)
        duty = angle / 18 + 2
        pwm.ChangeDutyCycle(duty)
        
    def moveServos(self, ang1, ang2, ang3):
        self.setAngle(ang1, self.Pwm1a)
        self.setAngle(180 - ang1, self.Pwm1b)
        self.setAngle(ang2, self.Pwm2a)
        self.setAngle(180 - ang2, self.Pwm2b)
        self.setAngle(ang3, self.Pwm3)
        sleep(5)
    
    def go_to_initial_pos(self):
        self.moveServos(self.theta1, self.theta2, self.theta3)
 