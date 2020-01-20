# -*- coding: utf-8 -*-
#import modules
import smbus
import math
from time import sleep

# slave address
DEV_ADDR = 0x68         # device address
# register address
ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47
PWR_MGMT_1 = 0x6b       # PWR_MGMT_1
PWR_MGMT_2 = 0x6c       # PWR_MGMT_2

bus = smbus.SMBus(1)
#unlock sleep
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)


#1byte read
def read_byte(adr):
    return bus.read_byte_data(DEV_ADDR, adr)
#2byte read
def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val
#sensor data read
def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):         # minus
        return -((65535 - val) + 1)
    else:                       # plus
        return val

#get temprature data
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53
    return x

#get gyro data(full scale range ±250 deg/s)
#LSB sensitivity 131 LSB/deg/s -> ±250 x 131 = ±32750 LSB[expressed by 16bit]); Gyroscope Configuration GYRO_CONFIG (reg=0x1B)
def get_gyro_data_lsb():
    x = read_word_sensor(GYRO_XOUT)
    y = read_word_sensor(GYRO_YOUT)
    z = read_word_sensor(GYRO_ZOUT)
    return [x, y, z]

def get_gyro_data_deg():
    x,y,z = get_gyro_data_lsb()
    x = x / 131.0
    y = y / 131.0
    z = z / 131.0
    return [x, y, z]

#get accelearation data(full scale range ±2g)
#LSB sensitivity 16384 LSB/g) -> ±2 x 16384 = ±32768 LSB[expressed by 16bit]); Accelerometer Configuration ACCEL_CONFIG (reg=0x1C)
def get_accel_data_lsb():
    x = read_word_sensor(ACCEL_XOUT)
    y = read_word_sensor(ACCEL_YOUT)
    z = read_word_sensor(ACCEL_ZOUT)
    return [x, y, z]

def get_accel_data_g():
    x,y,z = get_accel_data_lsb()
    x = x / 16384.0
    y = y / 16384.0
    z = z / 16384.0
    return [x, y, z]

#calcurate tilt 3-axis angle by accelearation; θ = 水平線とX軸との角度, Ψ = 水平線とy軸との角度, Φ = 重力ベクトルとz軸との角度
def calc_slope_for_accel_3axis_deg(x, y, z): # degree
    #calcurate θ
    theta = math.atan( x / math.sqrt( y*y + z*z ) )
    #calcurate Ψ
    psi = math.atan( y / math.sqrt( x*x + z*z ) )
    #calcurate Φ
    phi = math.atan( math.sqrt( x*x + y*y ) / z )
    deg_theta = math.degrees( theta )
    deg_psi   = math.degrees( psi )
    deg_phi   = math.degrees( phi )
    return [deg_theta, deg_psi, deg_phi]


def readData():
    #gyro data
    gyro_x,gyro_y,gyro_z = get_gyro_data_deg()
    #accelearation data
    gravity_x,gravity_y,gravity_z = get_accel_data_g()
    accel_x,accel_y,accel_z = gravity_x*9.81, gravity_y*9.81, gravity_z*9.81
    #tilt angle by accalearation
    theta,psi,phi = calc_slope_for_accel_3axis_deg(gravity_x,gravity_y,gravity_z)
    return str(accel_x) + "," + str(accel_y) + "," + str(accel_z) + "," + str(gyro_x) + "," + str(gyro_y) + "," + str(gyro_z) + "," + str(theta) + "," + str(psi) + "," + str(phi)


if __name__ == '__main__':
    try:
        readData()
    except KeyboardInterrupt:
        pass