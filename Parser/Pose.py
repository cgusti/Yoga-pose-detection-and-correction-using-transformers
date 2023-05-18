from BodyPart import BodyPart
import numpy as np
class Pose:
    #based on COCO dataset
    BODY_PART_NAMES = ['nose', 'left_eye', 'right_eye', 'left_ear', 
                       'right_ear', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
                       'left_wrist', 'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee',
                       'left_ankle', 'right_ankle'] 
    def __init__(self, body_parts):
        """
        Constructs a pose for one frame, given an array of parts 
        Parameters: 
            body_parts: 17 x 3 ndarray of x, y, confidence values
        """
        for name, vals in zip(self.BODY_PART_NAMES, body_parts):
            setattr(self, name, BodyPart(vals))

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value
    
    def __str__(self):
        out = ''
        for name in self.BODY_PART_NAMES:
            _ = "{}: {},{}".format(name, getattr(self, name).x, getattr(self, name).x)
            out = out + _ + '\n'
            return out
    
    def print(self, parts):
        """
        Print x and y coordinates of body parts on the current instance of the class
        Parameters: 
            parts: list 
                   list containing sequence of body parts E.g. ['nose', 'left ear']
        Returns: 
            x and y coordinates of each bodypart as set in construction time
        """
        out = ''
        for name in parts:
            if not name in self.BODY_PART_NAMES:
                raise NameError(name)
            _ = "{}: {},{}".format(name, getattr(self, name).x, getattr(self, name).y)
            out = out + _ + '\n'
        print(out)
        return out
            
if __name__ == '__main__':
    array = np.load('/home/cgusti/ViTPose_pytorch/data/result/numerical/downward_dog_7_result_array.npy')
    new_array = array.reshape(17, 3)
    pose = Pose(new_array)  
    #testing out class instances 
    pose.print(['nose', 'left_eye'])
    