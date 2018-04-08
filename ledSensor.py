from picamera.array import PiRGBAnalysis
from picamera.color import Color
from picamera.encoders import PiVideoFrame
import numpy as np
from datetime import datetime, date, time
import time
from Queue import Queue
from piLearning import piLearning

from gpiozero import Buzzer

import csv

# sensing and processing
class ledSensor(PiRGBAnalysis):
    def __init__(self, camera=None):
        super(ledSensor, self).__init__(camera)
        self.status = ''  # initialise as 0 or off
##        self.buzzer = Buzzer(22)
        self.pi_learn = piLearning()

        self.framecount = 0

        self.prevstat = ''
        self.sample_framecount = 0
        self.found_the_one = False

        self.prev_frame = ''


    def compare_data(self, ledstat):
        if (self.prevstat == 0 and ledstat ==1):
            if (self.found_the_one == False):
                self.found_the_one = True
            else:
                self.sample_framecount += 1
                self.pi_learn.event_queue.enqueue(self.sample_framecount) # add sample
                self.sample_framecount = 0  # reset framecount to zero
                self.pi_learn.event_queue.show_items()
        else:
            self.sample_framecount += 1
            
        
    def analyze(self, frame_array): # frame by frame analysis..

        mean_color = Color(
            r = int( np.mean( frame_array[31:34, 31:34, 0] ) ),
            g = int( np.mean( frame_array[31:34, 31:34, 1] ) ),
            b = int( np.mean( frame_array[31:34, 31:34, 2] ) )
            )

        h, l, s = mean_color.hls #convert color to HSL representation

    
        tmpStatus = 0
        if (l > 0.2):
            tmpStatus = 1
        else:
            tmpStatus = 0

        self.prev_frame = mean_color1
        ################################################################


        if tmpStatus != self.prevstat:
            self.prevstat = tmpStatus
            print(self.prevstat)
            print("ana")

        print(tmpStatus)
        return tmpStatus









##        self.framecount += 1
##        print("--------frame: " + str(self.framecount) + "LED: " + str(tmpStatus))

##        self.output_to_file( [self.framecount, tmpStatus] )
##        if tmpStatus != self.status:
####            if tmpStatus == 1:
####                self.buzzer.on()
####                time.sleep(0.1)
####                self.buzzer.off()
####                
##            self.status = tmpStatus
##            light_event = (self.status, datetime.now())
##            self.pi_learn.event_queue.enqueue(light_event)
##
##            self.pi_learn.learn()
##            

    def output_to_file(self, output):
        with open("onetwothree.txt", 'a') as newfile:
            file_writer = csv.writer(newfile)
            file_writer.writerow(output)


    
