import time
import picamera
import numpy as np
import os
import cv2

#何コマ撮るか変更
how_many_images = 100
###


cam = picamera.PiCamera()
cam.resolution = (1600,900)
cam.framerate = 5

cam.start_preview()
time.sleep(0.5)

cam.start_recording("video.h264")
cam.wait_recording(how_many_images)

cam.stop_recording()
cam.stop_preview

print("capture completed")

cap = cv2.VideoCapture("video.h264")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi",fourcc, 5, (1600,900))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        
        out.write(frame)
    
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
    
cap.release()
out.release()

print("rotate completed")
    
    