import numpy as np

class BodyPart: 
    def __init__(self, body_part):
        """
        Constructor for 1 body part consisting of x, y coordinates, confidence, and boolean exists information 
        Parameters: 
        body_part: int 
                   1 x 3 ndarray consisteing of x, y, confidence level
        """
        self.x = body_part[0]
        self.y = body_part[1]
        self.c = body_part[2]
        self.exists = self.c != 0 #check if body part exists or not within one frame
     
    def __truediv__(self, scalar):
        return BodyPart([self.x/scalar, self.y/scalar, self.c])
    
    def __floordiv__(self, scalar):
        __truediv__(self, scalar)
            
    @staticmethod
    def dist(bodypart1, bodypart2):
        "Calculates the Euclidean distance between BodyPart instances"
        return np.sqrt(np.square(bodypart1.x - bodypart2.x) + np.square(bodypart1.y - bodypart2.y))
        
        
    
    