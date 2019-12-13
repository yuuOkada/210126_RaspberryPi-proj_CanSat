# -*- coding: utf-8 -*-
import os
import time
import datetime
import numpy as np
import cv2
import picamera

loop_counter = 0

if not os.path.exists("./fetchedData"):
    os.mkdir("./fetchedData")

while loop_counter < 5:
    
    now_date = datetime.datetime.now().strftime('%Y%m%d')
    
    filename = str(now_date) + "_" + str(loop_counter)
    
    with picamera.PiCamera() as cam:
        cam.resolution = (1280,720)
        cam.start_preview()
        time.sleep(0.05)
        cam.capture(filename + ".jpg")
    
    img = cv2.imread(filename + ".jpg")

    rotated_img = cv2.rotate(img, cv2.ROTATE_180)
    cv2.imwrite(filename + ".jpg", rotated_img)

    sphere_index = 0
    sphere_list = []

    for vartical_num in range(10, 610, 100):
        for horizontal_num in range(40, 1140, 100):

            if not os.path.exists('./fetchedData/'+ str(sphere_index)):
                os.mkdir("./fetchedData/" + str(sphere_index))

            sphere_list.append(rotated_img[vartical_num:vartical_num+99, horizontal_num:horizontal_num+99])
            cv2.imwrite("./fetchedData/" + str(sphere_index) + "/" + filename, sphere_list[sphere_index])

            sphere_index += 1

    time.sleep(0.1)

    loop_counter += 1
