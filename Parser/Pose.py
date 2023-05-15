from .BodyPart import BodyPart

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
        out = ''
        for name in parts:
            if not name in self.BODY_PART_NAMES:
                raise NameError(name)
            _ = "{}: {},{}".format(name, getattr(self, name).x, getattr(self, name).y)