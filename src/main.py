from CV.cv import CV
from Motors.GPioServo import GPioServo
from Motors.Stepper import Stepper
from Motors.IK import IK
from Motors.Gripper import Gripper
from Motors.InitServo import InitServo
import sys
import RPi.GPIO as GPIO
from time import sleep
import numpy as np

l1 = 22.5   #distance from surface to first joint
l2 = 17.8
l3 = 17.3

servo = GPioServo()
gripper = Gripper()
stepper = Stepper()
ik = IK(l1, l2, l3)


def move_bot(x, y, phi):
    
    GPioServo.start_gpio(servo)
    GPioServo.go_to_initial_pos(servo)
    print('Finished Checkpoint 1: ')
    Gripper.runGripper(gripper)
    Stepper.initiateStepper(stepper)
    Stepper.AngleRotate(x, y)
    print('Finsihed Checkpoint 2: Stepper.')
    ang1, ang2, ang3 = ik.get_pos(x, y, phi)
    # print(ang1, ang2, ang3)
    GPioServo.moveServos(ang1, ang2, ang3)
    Gripper.openGripper(gripper)
    Gripper.closeGripper(gripper)
    ang1b, ang2b, ang3b = ik.get_pos(-5, -10, 180) 
    GPioServo.moveServos(ang1b, ang2b, ang3b)
    Gripper.openGripper(gripper)
    GPioServo.go_to_initial_pos(servo)


if __name__ == '__main__':

    x, y, phi = sys.argv[1], sys.argv[2], sys.argv[3]
    print(move_bot(x, y, phi))

   
        


    
