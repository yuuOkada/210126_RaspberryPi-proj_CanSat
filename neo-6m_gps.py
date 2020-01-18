# -*- coding: utf-8 -*-
import serial
import os
 
firstFixFlag = False
# will go true at first fix
firstFixDate = ""
 
# Set up serial:
ser = serial.Serial(
    port='/dev/ttyACA0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)
 
# Helper function to take HHMM.SS,
# Hemisphere and make it decimal:
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""
 
# Helper function to take a $GNGGA sentence,
# and turn it into a Python dictionary.
# This also cals degrees_to_decimal and stores
# the decimal values as well.
def parse_GNGGA(data):
    data = data.split(',')
    dict = {
            'fix_time': data[1],
            'latitude': data[2],
            'latitude_hemisphere': data[3],
            'longtitude': data[4],
            'longtitude_hemisphere': data[5],
            'quality': data[6],
            'satellites_num': data[7],
            'horizontal_qual': data[8],
            'absolute_hight': data[9],
            'meter_a': data[10],
            'geoidal_hight': data[11],
            'meter_g': data[12],
            'dgps_time': data[13],
            'checksum': data[14],
    }
 
    dict['decimal_latitude'] = degrees_to_decimal(dict['latitude'], dict['latitude_hemisphere'])
    dict['decimal_longtitude'] = degrees_to_decimal(dict['longtitude'], dict['longtitude_hemisphere'])
    return dict
 
# Main program roop:
while True:
    line = ser.readline()
    if byte(b"$GNGGA") in line: #This will exclude other NMEA sentences the GNSS provides.
        gpsData = parse_GNGGA(line) # Turn a GNGGA sentence into a Python dictionary called gpsData
        if gpsData['quality']=="1":
            # If the sentence shows that there's a fix, then we can log the line
            if firstFixFlag is False:
                # If we haven't found fix before , see the filename prefix with GPS data &amp; time.
                firstFixTime = gpsData['fix_time']
                firstFixFlag = True
            else: # write the data to a simple log file and then the raw data as well:
                with open("/home/pi/gnss_experimentation/" + firstFixTime + "-simple-log.txt", "a") as myfile:
                    simple_log_line = gpsData['fix_time'] + "," + str(gpsData['decimal_latitude']) + "," + str(gpsData['decimal_longtitude']) + "," + str(gpsData['absolute_hight'])
                    print (simple_log_line)
                    myfile.write(simple_log_line + "\n")
                with open ("/home/pi/gnss_experimentation/" + firstFixTime + "-GNGGA-raw-log.txt", "a") as myfile:
                    myfile.write(line)