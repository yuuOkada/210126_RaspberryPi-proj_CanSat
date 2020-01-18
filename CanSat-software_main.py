# -*- coding: utf-8 -*-
import bme280_i2c_def
import mpu6050_def
import Cam
import datetime
import time
import picamera
import os
 
dir_path = '/home/pi/FetchedData'
if not os.path.exists('/home/pi/FetchedData'):
    os.makedirs('/home/pi/FetchedData')

i = 0

while True:

    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d')
    label = now.strftime('%Y.%m.%d.%H:%M:%S')
    #BME280 & MPU6050
    csv = bme280_i2c_def.readData() + "," + mpu6050_def.readData()
    f = open('/home/pi/FetchedData/'+filename+'_data.csv','a')
    f.write("'"+label+"',"+csv+"\n")

    if i%5 == 0:
        #Camera
        Cam.readData(label)

    time.sleep(0.2)

    i = i + 1

f.close()
