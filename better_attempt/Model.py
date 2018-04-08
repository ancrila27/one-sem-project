import math

class Model:
    def __init__(self):
        self.stdev = 0
        self.upperbound = 0
        self.lowerbound = 0

    def train_set(self, avglist, sigma):
        print("training initiated")

        self.stdev, self.mu = self.calculateStDev(avglist)
        self.getThreshold(self.stdev, self.mu, sigma)
        print("model training completed")

    def calculateStDev(self, avglist):
        grand_mean = sum(avglist) / len(avglist)

        var = 0
        for x in avglist:
            var += ((x - grand_mean)**2)

        sd = math.sqrt( var / len(avglist) )

        return sd, grand_mean

    def calculateThreshold(self, std, mu, sigma):
        self.upperbound = mu + sigma*std
        self.lowerbound = mu - sigma*std


            
    # return thresholds
        


##  def stdev(self, avglist):
##        grand_mean = sum(avglist) / len(avglist)
##        sd = sum( (x - grand_mean)**2 for x in avglist )
##        return math.sqrt( sd / len(avglist)-1 ), grand_mean
##
##
##    def set_thresholds(self, stdev, mu, sigma):
##        ul = mu + sigma*stdev
##        ll = mu - sigma*stdev        
