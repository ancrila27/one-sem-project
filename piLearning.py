from Queue import Queue
import ledSensor
from datetime import datetime
from datetime import timedelta
import numpy as np

class piLearning:
    def __init__(self):
        self.event_queue = Queue()

    def get_mean(self, itemlist):
        return sum(itemlist) / len(itemlist)

    def get_stdev(self, smeanlist):
        grand_mean = self.get_mean(smeanlist)

        stdev = 0
        for x in smeanlist:
            stdev += (x - grand_mean) ** 2

        return stdev
        

    def learn(self):
        print("Learning initiated")

        # calculate averages
        self.moving_average(self, 10)

    def moving_average(self, window_size):
        if (self.event_queue.size() >= window_size):
            samples = self.event_queue.consumeQ(window_size) # assuming samples is not empty
            avg = self.get_mean(samples)

            self.movavgs.append(avg)

    def rolling_std(self, mu, samples):
        self.movstd.append(np.std(samples, ddof=1))  # standard deviation for samples (instead of population)
        
            
        
        
            
            

