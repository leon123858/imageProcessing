import cv2
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--video_dir", default='../../sampleData/video_0.mp4',
                    help='video path')
parser.add_argument("--cache_dir", default='../../cache/frames',
                    help='frames saved path')
opt = parser.parse_args()
# Opens the Video file
os.makedirs(opt.cache_dir, exist_ok=True)
cap = cv2.VideoCapture(opt.video_dir)
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(opt.cache_dir + '/frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
