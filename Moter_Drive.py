# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import numpy as np
import os

GPIO.setmode( GPIO.BCM )

#Define Left motor PIN
PWMA=21
Ain1=16
Ain2=20

#Define Right motor PIN
PWMB=6
Bin1=19
Bin2=13

#Define motor permission PIN
STBY=26

#motor PIN setup
m_list=[PWMA,Ain1,Ain2,STBY,PWMB,Bin1,Bin2]
GPIO.setup(m_list, GPIO.OUT, initial=GPIO.LOW )


#駆動モータ制御関数
def Moter_L(Duty):
    if Duty >= 0:
        GPIO.output( STBY, 1 )
        GPIO.output( Ain1, 0 )
        GPIO.output( Ain2, 1 )
        p_A.ChangeDutyCycle(Duty)
    else:
        Duty = abs(Duty)
        GPIO.output( STBY, 1 )
        GPIO.output( Ain1, 1 )
        GPIO.output( Ain2, 0 )
        p_A.ChangeDutyCycle(Duty)

#操舵モータ制御関数
def Moter_R(Duty):
    if Duty >= 0:
        GPIO.output( STBY, 1 )
        GPIO.output( Bin1, 0 )
        GPIO.output( Bin2, 1 )
        p_B.ChangeDutyCycle(Duty)
    else:
        Duty = abs(Duty)
        GPIO.output( STBY, 1 )
        GPIO.output( Bin1, 1 )
        GPIO.output( Bin2, 0 )
        p_B.ChangeDutyCycle(Duty)

print("set ini para")

#PWM Settings
p_A = GPIO.PWM(PWMA, 1000);
p_B = GPIO.PWM(PWMB, 1000);


#PWM Initialize
p_A.start(0)
p_B.start(0)

Moter_L(100)
Moter_R(100)
time.sleep(5)

#Shutdown
p_A.stop()
p_B.stop()
GPIO.cleanup()
