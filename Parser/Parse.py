import numpy as np
import argparse
import glob 
import os 
import cv2

from .PoseSequence import PoseSequence

def main():
    parser = argparse.ArgumentParser(description='Pose Parser')
    parser.add_argument('--input_folder', type=str, default='poses', help='input folder for image frames from video')
    parser.add_argument('--output_folder', type=str, default='poses_compressed', help='output folder for npy files')
    
    args = parser.parse_args()
    
    #load video 
    video_paths = glob.glob(os.path.join(args.input_folder, '*'))
    video_paths = sorted(video_paths)
    


def load_video(video_path):
    """loads a video from and splits into different image frames"""
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f'Error opening video file: {video_path}')
        return []
    frames = []
    while True: 
        ret, frame = video.read()
        #If the frame was not read successfully, then we have reached the end of the video
        if not ret: 
            break
        frames.append(frame)
    #Release the video object
    video.release()
    print('Number of frames: ')
    return frames
    
def parse_video_sequence():
    

# def load_ps(filename):
#     """
#     Load a PoseSequence object from a given numpy file. 
#     Parameters: 
#     filename: str 
#               file name of the numpy file constaining keypoints
#     Returns: 
#         PoseSequence object with normalized joint keypoints 
#     """
    
#     all_keypoints = np.load(filename)
