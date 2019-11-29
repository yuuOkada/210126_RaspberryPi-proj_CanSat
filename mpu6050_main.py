#coding: utf-8
 
import mpu6050_def
import datetime
import os
 
dir_path = '/home/pi/FetchedData'
 
now = datetime.datetime.now()
filename = now.strftime('%Y%m%d')
label = now.strftime('%Y.%m.%d.%H:%M')
csv = mpu6050_def.readData()
 
if not os.path.exists('/home/pi/FetchedData'):
    os.makedirs('/home/pi/FetchedData')
f = open('/home/pi/FetchedData'+filename+'_mpu6050.csv','a')
f.write("'"+label+"',"+csv+"\n")
f.close()