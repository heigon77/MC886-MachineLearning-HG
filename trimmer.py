
import csv

with open('countries_of_the_world.csv') as arq:
    
    count = 0
    reader = csv.reader(arq, delimiter=',')

    for line in reader:

        if count == 0:
            cols = len(line)
        else:
            print(len(line))