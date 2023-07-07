import numpy as np
from Pose import Pose
from BodyPart import BodyPart

class PoseSequence:
    """Contains a sequence of chained Pose Objects + normalization 
    based on average torso length"""
    def __init__(self, sequence):
        """
        Parameters: 
        sequence: list of 17x3 arrays 
        """
        self.poses = []
        for parts in sequence:
            self.poses.append(Pose(parts))
        
        #normalize poses based on the average pixel length
        torso_lengths = np.array([BodyPart.dist(pose.neck, pose.left_hip) for pose in self.poses if pose.neck.exists and pose.left_hip.exists] +
                                 [BodyPart.dist(pose.neck, pose.right_hip) for pose in self.poses if pose.neck.exists and pose.right_hip.exists])     
        mean_torso = np.mean(torso_lengths)   
        
        for pose in self.poses: 
            for attr, part in pose: 
                setattr(pose, attr, part/mean_torso)    

# if __name__ == '__main__':
#     pass