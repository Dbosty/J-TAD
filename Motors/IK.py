import numpy as np
import math
from numpy import *

class IK():

    #lengths of links
    l0 = None #distance from surface to first joint
    l1 = None
    l2 = None
    l3 = None

    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def get_pos(self, x, y, phi):
        x = float(x)
        y = float(y)
        phi = float(phi)
        
        # Converts cos and sin from radians to degrees
        degC= math.cos(math.radians(phi))
        degS = math.sin(math.radians(phi))

        wx = x - self.l3 * degC
        wy = y - self.l3 * degS
        delta = wx**2 + wy**2
    
        costheta2 = (delta - self.l1**2 - self.l2**2) / (2* self.l1 * self.l2)
        
        sintheta2 = np.sqrt(1 - costheta2**2)
        
        theta2 = math.atan(sintheta2/costheta2)
        theta2 = math.degrees(theta2)
        
        sintheta1 = ((self.l1 + self.l2 * costheta2) * wy - self.l2 * sintheta2 * wx) / delta
        
        costheta1 = ((self.l1 + self.l2 * costheta2) * wx + self.l2* sintheta2 * wy) / delta
        
        theta1 = arctan2(sintheta1, costheta1)
        theta1 = math.degrees(theta1)
        
        theta3 = phi - theta1 - theta2
        
        return theta1, theta2, theta3
    

  
