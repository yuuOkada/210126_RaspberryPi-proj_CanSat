# -*- coding: utf-8 -*-
import os
import time
import picamera

#read data
def readData(filename):
    #take picture in resolution(800,450)
    with picamera.PiCamera() as cam:
        cam.resolution = (800,450)
        cam.start_preview()
        time.sleep(0.02)
        cam.capture('/home/pi/FetchedData/' + filename + ".jpg")
    return


if __name__ == '__main__':
    try:
        readData()
    except KeyboardInterrupt:
        pass