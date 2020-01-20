# -*- coding: utf-8 -*-
#import modules
from gps3 import gps3

#
def readData():
    #define global variable
    global time, latitude, longtitude, altitude, speed
    #connnect to GPSdata
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()

    #if new data is exist on gps_socket
    for new_data in gps_socket:
        #unpack data
        if new_data:
            data_stream.unpack(new_data)
            #if data is "n/a" try one more
            if data_stream.TPV['lat'] != "n/a"
                time = str(data_stream.TPV['time'])
                latitude = str(data_stream.TPV['lat'])
                longtitude = str(data_stream.TPV['lon'])
                altitude = str(data_stream.TPV['alt'])
                speed = str(data_stream.TPV['speed'])
                print(time)
                return time + "," + latitude + ","  + longtitude + "," + altitude + "," + speed

if __name__ == "__main__":
    try:
        readData()
    except KeyboardInterrupt:
        pass