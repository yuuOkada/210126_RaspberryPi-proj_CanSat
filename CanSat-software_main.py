# -*- coding: utf-8 -*-
#import modules
import bme280_i2c_def
import mpu6050_def
import neo6m_gps3
import Cam
import datetime
import time
import picamera
import os
 
#file directory path
dir_path = '/home/pi/FetchedData'
if not os.path.exists('/home/pi/FetchedData'):
    os.makedirs('/home/pi/FetchedData')

i = 0

#Loop
while True:
    #timestamp
    now = datetime.datetime.now()
    #define filename from timestamp
    filename = now.strftime('%Y%m%d')
    label = now.strftime('%Y.%m.%d.%H.%M.%S')
    #fetch Temp,Hum,Atm & Accelearation,Gyro & GPS data
    csv = bme280_i2c_def.readData() + "," + mpu6050_def.readData() + "," + neo6m_gps3.readData()
    #save data to a .csv file
    f = open('/home/pi/FetchedData/'+filename+'_data.csv','a')
    f.write("'"+label+"',"+csv+"\n")
    f.close()

    #take picture every 5times
    if i%2 == 0:
        #Camera
        Cam.readData(label)

    i = i + 1