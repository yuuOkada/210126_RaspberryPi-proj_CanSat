#coding: utf-8
 
import bme280_i2c_def
import mpu6050_def
import datetime
import time
import os
 
dir_path = '/home/pi/FetchedData'
if not os.path.exists('/home/pi/FetchedData'):
    os.makedirs('/home/pi/FetchedData')

for i in range(10):
    now = datetime.datetime.now()
    filename = now.strftime('%Y%m%d')
    label = now.strftime('%Y.%m.%d.%H:%M:%S')
    #BME280 & MPU6050
    csv = bme280_i2c_def.readData() + "," + mpu6050_def.readData()
    f = open('/home/pi/FetchedData/'+filename+'_data.csv','a')
    f.write("'"+label+"',"+csv+"\n")
    #Camera
    picname = str(label)
    with picamera.PiCamera() as cam:
        cam.resolution = (1600,900)
        cam.start_preview()
        time.sleep(0.05)
        cam.capture('/home/pi/FetchedData/' + picname + ".jpg")
f.close()
