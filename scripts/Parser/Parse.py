import numpy as np
import argparse
import glob 
import os 
import cv2
import re
import sys
from PoseSequence import PoseSequence


import glob 
import torch
# from ..configs.ViTPose_base_coco_256x192 import model as model_cfg
# from ..configs.ViTPose_base_coco_256x192 import data_cfg
from inference import inference
from configs.ViTPose_base_coco_256x192 import model as model_cfg
sys.path.insert(0, '/home/cgusti/ViTPose_pytorch/scripts')

def parse_sequence(input_folder, output_folder):
    """
    Parse a sequence of image frames and saves each corresponding 
    pose from each image frame as a numpy file within the output directory
    
    Parameters: 
        input_folder: str 
                      path to the folder containing spliced image frames for one video
        output_folder: str 
                      path to saved numpy array files of keypoints 
    """
    def find_file_path(file_name):
        file_paths = glob.glob('**/' + file_name, recursive=True)
        if file_paths:
            return file_paths[0]
        raise ValueError('Missing value: data (filepath) is None')
    
    file_names = os.listdir(input_folder)
    num_frames = len(file_names)
    all_keypoints = np.zeros((num_frames, 17, 3))
    
    #set variables for model inference
    CUR_DIR = os.path.dirname(__file__)
    CKPT_PATH = "/home/cgusti/ViTPose_pytorch/checkpoints/vitpose-b-multi-coco.pth"
    # img_size = data_cfg['image_size']
    
    for i, file_name in enumerate(file_names):
        img_path = find_file_path(file_name)
        #model inference
        keypoints = inference(img_path=img_path, output_path=output_folder, img_size=img_size, 
                              model_cfg=model_cfg, ckpt_path=CKPT_PATH, device=torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu'), 
                              save_result=True) #this function will automatically save result in output path
        all_keypoints[i] = keypoints.reshape((17,3))
    yoga_pose_name = re.sub(r'\d+', '', os.path.basename(file_names[0]))
    pose_sequence_output_dir =  os.path.join(output_folder, yoga_pose_name + '_sequence')
    np.save(pose_sequence_output_dir, all_keypoints)
    
def load_ps(filename):
    '''
    Load a PoseSequence object from a given numpy file. 
    
    Args:
        filename: file name of the numpy file containing a sequence of keypoints from video
        
    Returns: 
        PoseSequence object with normalized keypoints.
    '''
    
    all_keypoints = np.load(filename)
    return PoseSequence(all_keypoints)

if __name__ == '__main__':
    parse_sequence(input_folder='/home/cgusti/ViTPose_pytorch/scripts/data/input_frames', output_folder='./data/result')
    