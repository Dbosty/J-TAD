
class InitServo():

    # Initial angles
    ### initialize angles with the real hardcoded angles
    theta1 = 40
    theta2 = 65    
    theta3 = 180  

    def __init__(self):
        self
        # self.theta1 = theta1
        # self.theta2 = theta2
        # self.theta3 = theta3

    def go_to_initial_pos(self):
        self.setAngle(self.theta1, self.Pwm1a)
        self.setAngle(180 - self.theta1, self.Pwm1b)
        self.setAngle(self.theta2, self.Pwm2a)
        self.setAngle(180 - self.theta2, self.Pwm2b)
        self.setAngle(self.theta3, self.Pwm3)
        





        
