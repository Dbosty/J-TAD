import numpy as np

class kinematic_functions():

    
    cap = None



    def __init__(self, cap):
        self.cap = cap


    def skew_3d(self, omega):
        """
        Converts a rotation vector in 3D to its corresponding skew-symmetric matrix.
        
        Args:
        omega - (3,) ndarray: the rotation vector
        
        Returns:
        omega_hat - (3,3) ndarray: the corresponding skew symmetric matrix
        """
        return np.array([[0, -omega[2], omega[1]], [omega[2], 0, -omega[0]], [-omega[1], omega[0], 0]])

    
    def rotation_3d(self, omega, theta):
        """
        Computes a 3D rotation matrix given a rotation axis and angle of rotation.
        
        Args:
        omega - (3,) ndarray: the axis of rotation
        theta: the angle of rotation
        
        Returns:
        rot - (3,3) ndarray: the resulting rotation matrix
        """
        if np.linalg.norm(omega) == 0:
            return np.eye(3)

        omega_hat = self.skew_3d(omega)
        norm = np.linalg.norm(omega)

        return np.eye(3) + ((omega_hat / norm) * np.sin(norm * theta)) + ((np.matmul(omega_hat, omega_hat) / norm**2) * (1 - np.cos(norm * theta)))


    def hat_3d(self, xi):
        """
        Converts a 3D twist to its corresponding 4x4 matrix representation
        
        Args:
        xi - (6,) ndarray: the 3D twist
        
        Returns:
        xi_hat - (4,4) ndarray: the corresponding 4x4 matrix
        """
        hat = None
        v = xi[:3]
        omega = xi[3:6]

        omega_hat = self.skew_3d(omega)

        hat[:3, :3] = omega_hat
        # hat[:3, 3] = ret_value

        return hat
        

    def homog_3d(self, xi, theta):
        """
        Computes a 4x4 homogeneous transformation matrix given a 3D twist and a 
        joint displacement.
        
        Args:
        xi - (6,) ndarray: the 3D twist
        theta: the joint displacement
        Returns:
        g - (4,4) ndarary: the resulting homogeneous transformation matrix
        """
        xi_hat = self.hat_3d(xi)
        g = np.linalg.expm(xi_hat*theta)

        return g

    def prod_exp(self, xi, theta):
        """
        Computes the product of exponentials for a kinematic chain, given 
        the twists and displacements for each joint.
        
        Args:
        xi - (6, N) ndarray: the twists for each joint
        theta - (N,) ndarray: the displacement of each joint
        
        Returns:
        g - (4,4) ndarray: the resulting homogeneous transformation matrix
        """
        result = self.homog_3d(xi.T[0], theta[0])
        index = 1
        for column in xi.T:
            if np.array_equiv(xi.T[0], column):
                continue
            theta_val = theta[index]
            exp = self.homog_3d(column, theta_val)
            result = np.matmul(result, exp)
            index += 1

        return result