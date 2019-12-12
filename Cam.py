import time
import picamera

with picamera.Picamera() as cam:
    cam.resolution(2400, 1800)
    cam.start_preview()
    time.sleep(2)
    cam.capture("1.jpg")
