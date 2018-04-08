import picamera
from ledanalyzer import ledanalyzer
from analysersample import analysersample
from Producer import Producer
import numpy

from collections import deque
import math
import time

class program:
    def __init__(self):
        self.q = deque(maxlen=10)
        self.camera = picamera.PiCamera()
        self.analyzer = ledanalyzer(self.camera)
       

    def start(self):
        self.camera.resolution = (32, 32)
        #self.camera.sensor_mode = 7
        self.camera.framerate = 30
        self.camera.zoom = (0.1, 0.1, 0.5, 0.5)
       

        self.camera.start_preview()

##        time.sleep(100)
##        self.camera.stop_preview()
##        self.camera.close()
        self.camera.start_recording(self.analyzer, 'yuv')
        try:
            while True:
                self.camera.wait_recording(1)
    
        finally:
            self.camera.stop_recording()
            self.camera.close()


if __name__ == "__main__":
    device = program()
    device.start()
    
