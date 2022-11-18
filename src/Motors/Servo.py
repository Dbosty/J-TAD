from Arm.ArmSetup import ArmConstants
from Arm.ArmControl import ArmSetup


class Servo():


    # Initializes the input of the Servo in the Raspberry Pi as well as 
    # joint names and their positions
    input = None
    servo_kit = None
    init_position = None



    def __init__(self, servo_kit, input, init_position):
        self.servo_kit = servo_kit
        self.input = input
        self.init_position = init_position


    def go_to_pos(self, angle):
        self.servo_kit.servo[self.pin].angle = angle

    def go_to_init_pos(self):
        self.go_to_pos(self.rest)

    # Returns J-Tad to their initial position
    def initial_position(self):
        ArmSetup.left_shoulder
        ArmSetup.right_shoulder
        ArmSetup.elbow
        ArmSetup.wrist
        ArmSetup.end_effector 
        
