import os
import cv2
import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("--image_path", default='../../sampleData/image_1.jpg',
                    help='image path')
parser.add_argument("--cache_dir", default='../../cache/split',
                    help='save clip images')
opt = parser.parse_args()
os.makedirs(opt.cache_dir, exist_ok=True)

# 讀取圖檔
img = cv2.imread(opt.image_path)

h, w, _ = img.shape

h_step = math.floor(h/3)
w_step = math.floor(w/3)

crop_imgs = []
for i in range(3):
    for j in range(3):
        base_h = i*h_step
        base_w = j*w_step
        crop_imgs.append(img[base_h:base_h + h_step, base_w:base_w + w_step])
for i, v in enumerate(crop_imgs):
    cv2.imwrite(opt.cache_dir + "/frame{}.jpg".format(str(i)), v)
