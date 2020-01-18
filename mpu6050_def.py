# -*- coding: utf-8 -*-
import smbus            # use I2C
import math             # mathmatics
from time import sleep  # time module


# define

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
                        # Sleep解除.
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

# Sub function
# 1byte read
def read_byte(adr):
    return bus.read_byte_data(DEV_ADDR, adr)
# 2byte read
def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val
# Sensor data read
def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):         # minus
        return -((65535 - val) + 1)
    else:                       # plus
        return val

# 温度
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53      # data sheet(register map)記載の計算式.
    return x

# 角速度(full scale range ±250 deg/s
#        LSB sensitivity 131 LSB/deg/s -> ±250 x 131 = ±32750 LSB[16bitで表現])
#   Gyroscope Configuration GYRO_CONFIG (reg=0x1B) ; FS_SEL(Bit4-Bit3)でfull scale range/LSB sensitivityの変更可.

# get gyro data
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

# 加速度(full scale range ±2g
#        LSB sensitivity 16384 LSB/g) -> ±2 x 16384 = ±32768 LSB[16bitで表現])
#   Accelerometer Configuration ACCEL_CONFIG (reg=0x1C) ; AFS_SEL(Bit4-Bit3)でfull scale range/LSB sensitivityの変更可.

# get accel data
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

# 傾き計算(3軸の傾斜の計算) ; 完全な球体(θΨΦ)を測定できる.
# θ = 水平線とX軸との角度, Ψ = 水平線とy軸との角度, Φ = 重力ベクトルとz軸との角度
def calc_slope_for_accel_3axis_deg(x, y, z): # degree
    # θ（シータ）
    theta = math.atan( x / math.sqrt( y*y + z*z ) )
    # Ψ（プサイ）
    psi = math.atan( y / math.sqrt( x*x + z*z ) )
    # Φ（ファイ）
    phi = math.atan( math.sqrt( x*x + y*y ) / z )

    deg_theta = math.degrees( theta )
    deg_psi   = math.degrees( psi )
    deg_phi   = math.degrees( phi )
    return [deg_theta, deg_psi, deg_phi]


def readData():
    # 角速度 小数点以下第3位まで表示.
    gyro_x,gyro_y,gyro_z = get_gyro_data_deg()

    # 加速度 小数点以下第3位まで表示.
    gravity_x,gravity_y,gravity_z = get_accel_data_g()
    accel_x,accel_y,accel_z = gravity_x*9.81, gravity_y*9.81, gravity_z*9.81

    #傾き from 加速度(3axis)
    theta,psi,phi = calc_slope_for_accel_3axis_deg(gravity_x,gravity_y,gravity_z)

    return str(accel_x) + "," + str(accel_y) + "," + str(accel_z) + "," + str(gyro_x) + "," + str(gyro_y) + "," + str(gyro_z) + "," + str(theta) + "," + str(psi) + "," + str(phi)


if __name__ == '__main__':
    try:
        readData()
    except KeyboardInterrupt:
        pass