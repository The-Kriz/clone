import cv2
import numpy as np

cap = cv2.VideoCapture(1)
# read image from file
ret, frame = cap.read()
# get size of image
img_size = frame.shape[:2]
print(img_size)
