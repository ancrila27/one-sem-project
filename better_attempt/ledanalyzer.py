from picamera.array import PiRGBAnalysis
from picamera.array import PiYUVAnalysis
from picamera.color import Color
import numpy as np
from PIL import Image


class ledanalyzer(PiYUVAnalysis):
    def __init__(self, camera):
        super(ledanalyzer, self).__init__(camera)
        self.status = ''
        self.alist = []
        self.qbuffer = []
        self.prev_framecount = 0
        self.curr_framecount = 0
        self.framecount = 0

        self.sample_means = []
        self.framenum = []

       
    def mov_avg(self, stat):
        self.prev_framecount = self.curr_framecount
        self.curr_framecount = self.framecount  # set prev and curr framecount values

        diff = abs(self.prev_framecount - self.curr_framecount) # difference between current 1 and prev 1
        self.qbuffer.append(diff) # only append values equal to 1

        # get the moving average
        if len(self.qbuffer) == 10:
            self.sample_means.append(sum(self.qbuffer) / len(self.qbuffer))
            #print(self.sample_means)
           
        elif len(self.qbuffer) > 10:
            self.qbuffer.pop(0)
            self.sample_means.append(sum(self.qbuffer) / len(self.qbuffer))
            #print(self.sample_means)
            
        
        #print(self.qbuffer)

       
    def analyze(self, fa):
        mean_lum = int( np.mean( fa[10:20, 10:20, 0] ) ) # luminance value for the ROI

        tmp_status = 0
        if (mean_lum > 100):
            tmp_status = 1
        else:
            tmp_status = 0

        self.framecount += 1
        
        if tmp_status != self.status: # change in event (1->0, 0->1)
            self.status = tmp_status
            print(self.status)
          
            if tmp_status == 1: # only store ON events
                self.mov_avg(tmp_status)


    

        #31:34, 31:34
##        meanpx = Color(
##            r = int( np.mean( fa[10:20, 10:20, 0] ) ),
##            g = int( np.mean( fa[10:20, 10:20, 1] ) ),
##            b = int( np.mean( fa[10:20, 10:20, 2] ) )
##            )
##
##      
##
##        h,l,s = meanpx.hls
##        print(l)
##        
##        tmp_status = 0
##        if (l > 0.15):
##            tmp_status = 1
##        else:
##            tmp_status = 0
##
##
##        self.framecount += 1
##
####        im = Image.fromarray(fa)
####        im.save('test{0}.jpg'.format(self.framecount))
##        if tmp_status != self.status: # change in event (1->0, 0->1)
##            self.status = tmp_status
##            #print(self.status)
##            if tmp_status == 1: # only store ON events
##                self.mov_avg(tmp_status)
