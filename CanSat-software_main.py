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
    csv = bme280_i2c_def.readData() + "," + mpu6050_def.readData()
    f = open('/home/pi/FetchedData/'+filename+'_data.csv','a')
    f.write("'"+label+"',"+csv+"\n")
f.close()
