from picamera.array import PiRGBAnalysis
from picamera.color import Color
import numpy as np
from datetime import datetime
import time
from graphPlot import graphPlot

import csv

# sensing and processing
class ledSensor(PiRGBAnalysis):
    def __init__(self, camera):
        self.start_time = time.time()
        super(ledSensor, self).__init__(camera)
        self.a_graph = graphPlot()
        self.status = ''  # initialise as 0 or off
        self.prevlightness = 0        

    def analyze(self, frame_array):
        
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

        elapsed_time = time.time() - self.start_time

        if tmpStatus != self.status:
            arr = []
            self.status = tmpStatus
            arr.append(self.status)
            #arr.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            arr.append(elapsed_time)
            print( self.status )
            #print( elapsed_time )
            #self.a_graph.add_point(self.status, elapsed_time)
            self.output_to_file(arr)

    def output_to_file(self, output):
        with open("sample3.csv", 'a') as newfile:
            file_writer = csv.writer(newfile)
            file_writer.writerow(output)

    


