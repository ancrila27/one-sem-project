import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime


class graphPlot:
    def __init__(self):
        #initialise the graph entities
        style.use('fivethirtyeight')
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

##        self.xs = []
##        self.ys = []

    def animate(self, i):
        graph_data = open('sample3.csv', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []

        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(y)

        self.ax1.clear()
        self.ax1.step(ys, xs, linewidth=1, where='post')

    def show_graph(self):
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

##    def add_point(self, x, y):
##        self.xs.append(x)
##        self.ys.append(y)
##
##        self.ax1.clear()
##        self.ax1.plot(self.xs, self.ys)
##
##        print(self.xs)
##        print(self.ys)

##if __name__ == "__main__":
##    graph = graphPlot()
##    graph.show_graph()
##    
        
        

        
        
