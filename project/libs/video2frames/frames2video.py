import glob
import numpy as np
import cv2
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--frames_dir", default='../../cache/frames',
                    help='frames path')
parser.add_argument("--cache_dir", default='../../cache',
                    help='video saved path')
opt = parser.parse_args()
os.makedirs(opt.cache_dir, exist_ok=True)

count = len(glob.glob(opt.frames_dir + '/*.jpg'))
img_array = []
for i in range(count):
    img = cv2.imread(opt.frames_dir + "/frame{}.jpg".format(str(i)))
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter(
    opt.cache_dir + '/transfer.avi', cv2.VideoWriter_fourcc(*'MJPG'), 60.0, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
