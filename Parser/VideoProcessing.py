"""Takes in a video split it into different image frames"""

"""This is unfinished"""
import argparse
import cv2

def main(): 
    parser = argparse.ArgumentParsere(description='Video Pre-Processing')
    parser.add_argument('--input_video', type=str, default='', help='input video to be split into individual frames')
    parser.add_argument('--output_folder', type=str, default='', help='output directory to contain image frames')
    parser.add_argument('--yoga_pose_name', type=str)
    parser.add_argument('--correct', type=str, default='', help='Whether video is a correct or wrong yoga pose')
    args= parser.parse_args()

    load_video(args.input_video, args.output_folder, yoga_pose_name, correct)
    

def load_video(video_path, output_folder, yoga_pose_name):
    """loads a video from and splits into different image frames"""
    capture = cv2.VideoCapture(video_path)
    num_frames = 0
    while (True):
        success, frame = capture.read()
        if success:
            cv2.imwrite(f'./{output_folder}/{yoga_pose_name}/{num_frames}')
        else: 
            break
        num_frames +=1
    capture.release()


    