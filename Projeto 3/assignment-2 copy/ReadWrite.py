class ReadWrite():
    "Class CroosOver"

    pmt = []
    agentNum = 0

    def __init__(self):
        with open('agentNum.txt') as f:
            lines = f.readlines()
            self.agentNum = int(lines[0])

        with open('parameters.txt') as f:
            lines = f.readlines()
            
            self.pmt = lines[self.agentNum].split()

            for i in range(len(self.pmt)):
                if(1<=i<=9):
                    self.pmt[i] = int(self.pmt[i])
                else:
                    self.pmt[i] = float(self.pmt[i])
    
    def read(self):

        with open('results.txt') as f:
            lines = f.readlines()
            
            avgScore = []
            wins = []
            rate = []

            for i in range (3):
                line = lines[i].split()
                avgScore.append(line[0])
                wins.append(line[1])
                rate.append(line[2])

        with open('results.txt','w') as f:
            f.write("")
        
        with open('results.txt','a') as f:
            string = str((avgScore[0]+avgScore[2])/2) + " " + str(rating[0])  + " " + str(rating[1]) + '\n'
            f.write(string)
