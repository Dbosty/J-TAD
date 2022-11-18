from Arm.ArmSetup import ArmConstants
from Motors.Servo import Servo
from Motors.Stepper import Stepper

# Need to pip install this library still
# https://docs.circuitpython.org/projects/servokit/en/latest/
from adafruit_servokit import ServoKit
# https://gpiozero.readthedocs.io/en/stable/api_output.html
from gpiozero import AngularServo
# Need to pip install this library still
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-stepper-motors
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper


class ArmSetup():

    # Initializes the Raspberry Pi ServoKit and MotorKit we are using for the 
    # servos and the stepper motor
    servoKit = None
    stepperKit = None

    # Initializes the names of the Servos we are working with
    stepper = None
    left_shoulder = None
    right_shoulder = None
    elbow = None
    wrist = None
    end_effector = None

    
    def __init__(self):
        # How many channels does our Pi have???
        # Driver channels 
        self.servoKit = ServoKit(channels=...)
        self.stepperKit = MotorKit(channel=...)

        # Defines all the motors on J-Tad at initial position
        self.stepper = Stepper(self.stepperKit, ArmConstants.STEPPER_INPUT, ArmConstants.STEPPER_INIT_POS)
        self.left_shoulder = Servo(self.servoKit, ArmConstants.LEFT_SHOULDER_INPUT, ArmConstants.LEFT_SHOULDER_INIT_POS)
        self.right_shoulder = Servo(self.servoKit, ArmConstants.RIGHT_SHOULDER_INPUT, ArmConstants.RIGHT_SHOULDER_INIT_POS)
        self.elbow = Servo(self.servoKit, ArmConstants.ELBOW_INPUT, ArmConstants.ELBOW_INIT_POS)
        self.wrist = Servo(self.servoKit, ArmConstants.WRIST_INPUT, ArmConstants.WRIST_INIT_POS)
        self.end_effector = Servo(self.servoKit, ArmConstants.END_EFFECTOR_INPUT, ArmConstants.END_EFFECTOR_INIT_POS)
    

    def apply_to_all_servos(self, function):
        '''
        Applies an arbitrary function to all motors.

        Args: 
        function - any function you want applied to the motors

        Returns:

        '''
        function(self.left_shoulder)
        function(self.right_shoulder)
        function(self.elbow)
        function(self.wrist)
        function(self.end_effector)

    # def go_to_init_pos(self, angle):
        



