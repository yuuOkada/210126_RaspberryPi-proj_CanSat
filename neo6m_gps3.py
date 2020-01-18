# -*- coding: utf-8 -*-
from gps3 import gps3

def readData():
    global time, latitude, longtitude, altitude, speed
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()

    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            if data_stream.TPV['lat'] != "n/a"
                time = str(data_stream.TPV['time'])
                print(time)
                latitude = str(data_stream.TPV['lat'])
                longtitude = str(data_stream.TPV['lon'])
                altitude = str(data_stream.TPV['alt'])
                speed = str(data_stream.TPV['speed'])
                return time + "," + latitude + ","  + longtitude + "," + altitude + "," + speed

if __name__ == "__main__":
    try:
        readData()
    except KeyboardInterrupt:
        pass