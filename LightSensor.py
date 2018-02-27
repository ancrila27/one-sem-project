import picamera
import numpy as np
from picamera.array import PiRGBAnalysis
from picamera.color import Color
import math

class LightSensor(PiRGBAnalysis):
    def __init__(self, camera):
        super(LightSensor, self).__init__(camera)
        self.status = ''


    def analyze(self, a):
        # Convert the average color of pixels in the middle box
        c = Color(
            r=int(np.mean(a[30:60, 60:120, 0])),
            g=int(np.mean(a[30:60, 60:120, 1])),
            b=int(np.mean(a[30:60, 60:120, 2]))
            )

        brightness = math.sqrt(
            (c.red**2) * 0.241 +
            (c.green**2) * 0.691 +
            (c.blue**2) * 0.068
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
            self.status = c_status
            print(c_status)
        


with picamera.PiCamera(resolution='160x90', framerate=30) as camera:
    # fix camera's white-balance gains
    camera.awb_mode = 'off'
    camera.awb_gains = (1.4, 1.5)
    # draw a box over the area we're going to watch
    camera.start_preview() #alpha=128
    box = np.zeros((96, 160, 3), dtype=np.uint8)
    box[30:60, 60:120, :] = 0x80
    #construct the analysis output and start recording data to it
    with LightSensor(camera) as analyser:
        camera.start_recording(analyser, 'rgb')
        try:
            while True:
                camera.wait_recording(1)
        finally:
            camera_stop_recording()

