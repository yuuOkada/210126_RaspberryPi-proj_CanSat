# -*- coding: utf-8 -*-
import os
import time
import datetime
import picamera

def readData(filename):
    
    with picamera.PiCamera() as cam:
        cam.resolution = (1600,900)
        cam.start_preview()
        time.sleep(0.05)
        cam.capture('/home/pi/FetchedData/' + filename + ".jpg")

    return


if __name__ == '__main__':
    try:
        readData()
    except KeyboardInterrupt:
        pass