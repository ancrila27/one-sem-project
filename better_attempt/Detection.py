from gpiozero import Buzzer
import time

class Detection:
    def __init__(self):
        self.alarm = Buzzer(22)
        
    def findAnomalies(self, newData, mu, std, sigma):
        if (newData > (mu + sigma*std) | newData < (mu - sigma*std) ):
            print("Anomaly detected")
            self.alarm.on()
            time.sleep(3)
            self.alarm.off()
            
        else:
            print("Normal")

##    def anomaly(self, mean, std, x):
##        if abs(x-mean) > 3*std:
##            print("Anomaly detected")
##if __name__ == "__main__":
    
