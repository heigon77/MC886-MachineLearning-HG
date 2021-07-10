class ReadWrite():
    "Class that reads files"

    pmt = []
    agentNum = 0
    nome = ''

    def __init__(self):

        with open('nome.txt', 'r') as f:
            lines = f.readlines()
            self.nome = lines[0]

        with open('agentNum_' + self.nome + '.txt') as f:
            lines = f.readlines()
            self.agentNum = int(lines[0])

        with open('parameters_' + self.nome + '.txt') as f:
            lines = f.readlines()
            
            self.pmt = lines[self.agentNum].split()

            for i in range(len(self.pmt)):
                if(1<=i<=9):
                    self.pmt[i] = int(self.pmt[i])
                else:
                    self.pmt[i] = float(self.pmt[i])
    
    def read(self):

        with open('results_' + self.nome + '.txt') as f:
            lines = f.readlines()
            
            avgScore = []
            wins = []
            rate = []

            for i in range (3):
                line = lines[i].split()
                avgScore.append(line[0])
                wins.append(line[1])
                rate.append(line[2])

        with open('results_' + self.nome + '.txt','w') as f:
            f.write("")
        
        with open('results_' + self.nome + '.txt','a') as f:
            string = str((avgScore[0]+avgScore[2])/2) + " " + str(rating[0])  + " " + str(rating[1]) + '\n'
            f.write(string)

class ReadWriteBest():
    "Class that reads files"

    pmt = []
    agentNum = 0
    nome = ''

    def __init__(self):

        with open('nome.txt', 'r') as f:
            lines = f.readlines()
            self.nome = lines[0]

        with open('best_' + self.nome + '.txt', 'r') as f:
            lines = f.readlines()
            
            self.pmt = lines[self.agentNum].split()

            for i in range(len(self.pmt)):
                if(1<=i<=9):
                    self.pmt[i] = int(self.pmt[i])
                else:
                    self.pmt[i] = float(self.pmt[i])
    
    def read(self):

        with open('results_best_' + self.nome + '.txt') as f:
            lines = f.readlines()
            
            avgScore = []
            wins = []
            rate = []

            for i in range (3):
                line = lines[i].split()
                avgScore.append(line[0])
                wins.append(line[1])
                rate.append(line[2])

        with open('results_best_' + self.nome + '.txt','w') as f:
            f.write("")
        
        with open('results_best_' + self.nome + '.txt','a') as f:
            string = str((avgScore[0]+avgScore[2])/2) + " " + str(rating[0])  + " " + str(rating[1]) + '\n'
            f.write(string)
