from numpy.random import choice
import numpy as np
import random
import matplotlib.pyplot as plt

for layout in ["smallClassic", "mediumClassic", "originalClassic"]:
        Best = []
        Avg = []
        Wrst = []
        x = []
        with open('fitness_' + layout + '.txt', 'r') as f:
            lines = f.readlines()
            counter = 1
            for line in lines:
                line = line.split()
                Best.append(round(float(line[0]),2))
                Avg.append(round(float(line[1]),2))
                Wrst.append(round(float(line[2]),2))
                x.append(counter)
                counter+=1
            
        
        plt.plot(x, Best, label = 'Best') 
        plt.plot(x, Avg, label = 'Average')
        plt.plot(x, Wrst, label = 'Worst')
        plt.legend()
        plt.title("Gráfico de Fitness ao longo das gerações "+layout)
        plt.xlabel("Geração")
        plt.ylabel("Fitness")
        plt.savefig("graph"+layout+".png")