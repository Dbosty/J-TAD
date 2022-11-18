from Arm.ArmSetup import ArmConstants


class Stepper():


    # Initializes the input of the Servo in the Raspberry Pi as well as their positions
    stepperKit = None
    input = None
    position = None



    def __init__(self, stepperKit, input, position):
        self.stepperKit = stepperKit
        self.input = input
        self.position = position

    
    # Returns J-Tad to their initial position
    def go_to_pos(self, angle):
        self.stepperKit.angle = angle
    
    # def initial_pos(self):
    #     ArmConstants.s
