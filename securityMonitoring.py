import picamera
from ledSensor import ledSensor
from graphPlot import graphPlot

### main system execution
class securityMonitoring:
    def __init__(self):
        print("Initialising system...")

    def startSystem(self): #sensing/ data collection
        with picamera.PiCamera() as camera:
            camera.resolution = (64, 64)
            camera.framerate = 30
            camera.sensor_mode = 7
            print("Camera is warming up...")

            camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
            with ledSensor(camera) as analyzer:
                camera.start_recording(analyzer, 'rgb')
                try:
                    while True:
                        camera.wait_recording(1)
                     
                finally:
                    camera.stop_recording()

if __name__ == "__main__":
    print("**** **NON-INTRUSIVE SECURITY MONITORING SYSTEM** ****")
    device = securityMonitoring()
    try:
        device.startSystem()
    finally:
        a = graphPlot()
        a.show_graph()
        print("Failed to start")
