# -*- coding: utf-8 -*-
import os
import time
import datetime
import numpy as np
import cv2
import picamera

i = 0

while i < 5:
    
    now_time = datetime.datetime.now().strftime('%Y%m%d%H')
    
    filename = str(now_time) + "_" + str(i) + ".jpg"
    
    with picamera.PiCamera() as cam:
        #cam.resolution()
        cam.start_preview()
        time.sleep(0.2)
        cam.capture(filename)
    
    img = cv2.imread(filename)
    rotated_img = cv2.rotate(img, cv2.ROTATE_180)
    
    cv2.imwrite(filename, rotated_img)
    
    time.sleep(0.5)
    
    i += 1
