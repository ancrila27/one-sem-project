import picamera
import numpy as np
from picamera.array import PiRGBAnalysis
from picamera.color import Color
import math
from datetime import datetime

class LightSensor(PiRGBAnalysis):
    def __init__(self, camera):
        super(LightSensor, self).__init__(camera)
        self.status = ''


    def analyze(self, a):
       
        #c  = Color( a )
        # Convert the average color of pixels in the middle box
        c = Color(
            r=int(np.mean(a[30:60, 60:120, 0])),
            g=int(np.mean(a[30:60, 60:120, 1])),
            b=int(np.mean(a[30:60, 60:120, 2]))
            )
        
        # Convert the color to hue, saturation, lightness
        h, l, s = c.hls
        c_status = '---'
        #print(c_status)

        if l > 0.2:
            c_status = 'ON'
        else:
            c_status = 'OFF'

        if c_status != self.status:
            print(a.shape)
            self.status = c_status
            print(str(datetime.now()) + " (" + str(c_status) + ") L:" + str(l))


with picamera.PiCamera(resolution='64x64', framerate=30) as camera:
    camera.awb_mode = 'off'
    camera.awb_gains = (1.4, 1.5)

    camera.start_preview()
    with LightSensor(camera) as analyser:
        camera.start_recording(analyser, 'rgb')
        try:
            while True:
                camera.wait_recording(10000)
        finally:
            camera.stop_recording()

    
  
    # draw a box over the area we're going to watch
##    camera.start_preview() #alpha=128
##    box = np.zeros((96, 160, 3), dtype=np.uint8)
##    box[30:60, 60:120, :] = 0x80
    #construct the analysis output and start recording data to it
