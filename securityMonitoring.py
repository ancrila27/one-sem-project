import picamera
from ledSensor import ledSensor


class securityMonitoring:
    def __init__(self):
        print("Initialising system...")
        self.camera = picamera.PiCamera() # picamera instance
        self.analyser = ledSensor(self.camera) # frame analyser/processor

    def startSystem(self):
        print("Camera warming up")
        self.camera.resolution = (64,64)
        self.camera.framerate = 30
        
        print("Starting camera preview.")
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))

        self.camera.start_recording(self.analyser, 'rgb')
        try:
            while True:
                self.camera.wait_recording(1)
        finally:
            self.camera.stop_recording()

# MAIN:
if __name__ == "__main__":
    print("**** **NON-INTRUSIVE SECURITY MONITORING SYSTEM** ****")
    device = securityMonitoring()
    try:
        device.startSystem()
    finally:
        print()


        ##    def startSystem(self): #sensing/ data collection
##        with picamera.PiCamera() as camera:
##            camera.resolution = (64, 64)
##            camera.framerate = 30
##            camera.sensor_mode = 7
##            print("Camera is warming up...")
##
##            camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
##            with ledSensor(camera) as analyzer:
##                camera.start_recording(analyzer, 'rgb')
##                try:
##                    while True:
####                        print("frameindex: " + str(camera.frame.index))
##                        camera.wait_recording(1)
##                      
##                     
##                finally:
##                    camera.stop_recording()
