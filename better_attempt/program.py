import picamera
from ledanalyzer import ledanalyzer

import numpy

from collections import deque
import math
import time

import Model
import tty, sys, termios


class program:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.analyzer = ledanalyzer(self.camera)

    def stopCam(self):
        self.camera.stop_recording()
        self.camera.close()

    def start(self):
        self.camera.resolution = (32, 32)
        #self.camera.sensor_mode = 7
        self.camera.framerate = 30
        self.camera.zoom = (0.1, 0.1, 0.5, 0.5)
        self.camera.start_preview()


        self.camera.start_recording(self.analyzer, 'yuv')
        ##################################################
        try:
            while True:
                self.camera.wait_recording(1)
                #if (some key is pressed):
                 #   break loop
    
        finally:
            self.stopCam()
        ##################################################

        # training
        m = Model()
        m.train_set(self.analyzer.sample_means)

        # predict/detect
        # turn back camera on
      
        # then pass to detection
        # detector = Detection()
        


if __name__ == "__main__":
    device = program()
    device.start()
    
