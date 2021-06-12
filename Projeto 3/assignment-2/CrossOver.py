class CrossOver():
    "Class CroosOver"

    distCap = 0
    num7 = 0
    num3 = 0
    num5 = 0
    agentNum = 0

    def __init__(self):
        with open('agentNum.txt') as f:
            lines = f.readlines()
            self.agentNum = int(lines[0])

        with open('parameters.txt') as f:
            lines = f.readlines()
            
            self.distCap, self.num7, self.num3, self.num5 = map(int,lines[self.agentNum].split())
    
    def crossover():

        with open('results.txt') as f:
            lines = f.readlines()
            
            avgScore, wins, rate = map(int,lines[self.agentNum].split())
