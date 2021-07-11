from pacman import Directions
from game import Agent
import numpy as np
import random

class QLearnAgent(Agent):

    # Inicializa o Agent com os atributos necessários
    def __init__(self, numTraining = 10):

        # Parâmetros do Q-Learning 
        self.alpha = 0.2
        self.epsilon = 0.1
        self.gamma = 0.8
        self.qValues = dict()

        # Acompanha resultados durante o episódio
        self.numTraining = int(numTraining)
        self.episodesSoFar = 0
        self.actionsSoFar = 0
        self.totalReward = 0
        
        # Usado para criar estado e recompensas
        self.lastState = None
        self.lastAction = None
        self.lastScore = None
        self.lastNumFood = None
        self.lastCaps = None
        self.lastDistGhost = None
        self.lastDistFood = None
        self.doNotEat = None
        self.ghostWasNear = False
        self.lastFoodPosition = None

        # Escreve em arquivos diferente dependendo do número de treino
        if(self.getNumTraining() < 2500):
            with open('episodesResults3.txt','w') as f:
                f.write("")
        elif(self.getNumTraining() < 5500):
            with open('episodesResults2.txt','w') as f:
                f.write("")
        else:
            with open('episodesResults1.txt','w') as f:
                f.write("")


    # Funções para acessar os atributos

    def incrementEpisodesSoFar(self):
        self.episodesSoFar += 1

    def getEpisodesSoFar(self):
        return self.episodesSoFar
    
    def incrementAcionsSoFar(self):
        self.actionsSoFar += 1
    
    def getAcionsSoFar(self):
        return self.actionsSoFar

    def getNumTraining(self):
        return self.numTraining

    def setEpsilon(self, value):
        self.epsilon = value

    def getAlpha(self):
        return self.alpha

    def setAlpha(self, value):
        self.alpha = value

    def getGamma(self):
        return self.gamma

    
    # Cria o estado baseado em direções legais, distância do fantasma mais próximo e sua posição relativa e da comida mais próxima
    def createState(self,state,legal):
        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())
        posFood = state.getFood()
        numFood = state.getNumFood()

        minDistGhost = 99999
        indG = None
        for i in range(len(posG)):
            if(np.linalg.norm(posG[i]-posP) < minDistGhost):
                minDistGhost = np.linalg.norm(posG[i]-posP)
                indG =  i

        if(posG[indG][0] > posP[0]):
            if(posG[indG][1] > posP[1]):
                ghostRelativePosition = "upright"
            elif(posG[indG][1] == posP[1]):
                ghostRelativePosition = "right"
            else:
                ghostRelativePosition = "downright"

        elif(posG[indG][0] == posP[0]):
            if(posG[indG][1] > posP[1]):
                ghostRelativePosition = "up"
            else:
                ghostRelativePosition = "down"
        else:
            if(posG[indG][1] > posP[1]):
                ghostRelativePosition = "upleft"
            elif(posG[indG][1] == posP[1]):
                ghostRelativePosition = "left"
            else:
                ghostRelativePosition = "downleft"

        if(numFood > 0):
            minDistFood = 99999
            minFood = None
            for x in range(posFood.width):
                for y in range(posFood.height):
                    if(posFood[x][y]):
                        food = np.array([x,y])
                        distFood = np.linalg.norm(food-posP)
                        if(distFood<minDistFood):
                            minDistFood = distFood
                            minFood = food
            
            if(minFood[0] > posP[0]):
                if(minFood[1] > posP[1]):
                    foodRelativePosition = "upright"
                elif(minFood[1] == posP[1]):
                    foodRelativePosition = "right"
                else:
                    foodRelativePosition = "downright"

            elif(minFood[0] == posP[0]):
                if(minFood[1] > posP[1]):
                    foodRelativePosition = "up"
                else:
                    foodRelativePosition = "down"
            else:
                if(minFood[1] > posP[1]):
                    foodRelativePosition = "upleft"
                elif(minFood[1] == posP[1]):
                    foodRelativePosition = "left"
                else:
                    foodRelativePosition = "downleft"
            self.lastFoodPosition  = foodRelativePosition
        else:
            foodRelativePosition = self.lastFoodPosition

        if(minDistGhost < 3):
            ghostNear = True
        else:
            ghostNear = False
        
        # Retorna uma string descrevendo o estado
        return str(legal)+str(ghostNear)+str(ghostRelativePosition)+str(foodRelativePosition)

    # Caso o estado ainda não exista é gerado um para cada ação legal com valor Q = 0
    def initializeQValues(self, pacmanState, legal):
        self.qValues[pacmanState] = dict()
        for action in legal:
            if action not in self.qValues[pacmanState]:
                self.qValues[pacmanState][action] = 0.0

    # Calcula a recompensa da última ação e atualiza  valor Q do estado e sua ação através da função do Q-learning
    def updateQValue(self, state,pacmanState, final_step=False):
        
        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())
        posFood = state.getFood()

        numFoodEat = self.lastNumFood - state.getNumFood()
        numCapsEat = self.lastCaps - len(state.getCapsules())

        minDistGhost = 99999
        for i in range(len(posG)):
            if(np.linalg.norm(posG[i]-posP) < minDistGhost):
                minDistGhost = np.linalg.norm(posG[i]-posP)
        
        minDistFood = 99999
        for x in range(posFood.width):
            for y in range(posFood.height):
                if(posFood[x][y]):
                    food = np.array([x,y])
                    distFood = np.linalg.norm(food-posP)
                    if(distFood<minDistFood):
                        minDistFood = distFood

        if(self.ghostWasNear):
            if(minDistGhost >= self.lastDistGhost):
                didNotEat = 30
            else:
                didNotEat = -30
        else:
            if(numFoodEat == 0 or numCapsEat == 0):
                if(minDistFood > self.lastDistFood):
                    didNotEat = -15
                else:
                    didNotEat = 15
            else:
                didNotEat = 0

        reward = numFoodEat * 10 + numCapsEat * 20 + didNotEat
        self.totalReward += reward

        max_Q_value = 0.0
        if not final_step:
            max_Q_value = max(list(self.qValues[pacmanState].values()))
        self.qValues[self.lastState][self.lastAction] += (self.alpha * (reward + self.gamma * max_Q_value - self.qValues[self.lastState][self.lastAction]))

    # Escolha a nova ação balanceando exploration e exploitation
    def epsilonGreedy(self, state,pacmanState, legal):
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)

        if not self.ghostWasNear:
            if(self.lastAction!= None):
                if (Directions.REVERSE[self.lastAction] in legal) and len(legal)>1:
                    legal.remove(Directions.REVERSE[self.lastAction])

        probability = random.random()

        if probability < self.epsilon: # Escolhe ação aleatória
            random_action = random.choice(legal)
            return random_action

        max_Q_action = None # Escolhe a que já sabe ser melhor
        for action in legal:
            if max_Q_action == None:
                max_Q_action = action
            if self.qValues[pacmanState][action] > self.qValues[pacmanState][max_Q_action]:
                max_Q_action = action
        return max_Q_action
    
    # Atualiza atributos para um novo estado
    def updateAttributes(self, state,pacmanState, legal):

        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())
        posFood = state.getFood()

        self.lastNumFood = state.getNumFood()
        self.lastCaps = len(state.getCapsules())

        minDistGhost = 99999
        for i in range(len(posG)):
            if(np.linalg.norm(posG[i]-posP) < minDistGhost):
                minDistGhost = np.linalg.norm(posG[i]-posP)
        
        minDistFood = 99999
        for x in range(posFood.width):
            for y in range(posFood.height):
                if(posFood[x][y]):
                    food = np.array([x,y])
                    distFood = np.linalg.norm(food-posP)
                    if(distFood<minDistFood):
                        minDistFood = distFood
        
        if(minDistGhost <= 3.5 ):
            self.ghostWasNear = True
        else:
            self.ghostWasNear = False
        self.lastDistGhost = minDistGhost
        self.lastDistFood = minDistFood
        self.lastState = self.createState(state,legal)
        self.lastAction = self.epsilonGreedy(state,pacmanState, legal)
        self.lastScore = state.getScore()

    # Reseta todos atributos (no fim do episódio)
    def resetAttributes(self):
        self.totalReward = 0
        self.actionsSoFar = 0
        self.lastState = None
        self.lastAction = None
        self.lastScore = None

    # Escolhe uma ação, inicializa o estado que o pacman está caso não exista ainda e move o pacman
    def getAction(self, state):

        legal = state.getLegalPacmanActions()

        if Directions.STOP in legal: # Remove a ação de parar
            legal.remove(Directions.STOP)
        
        if not self.ghostWasNear: # Se não possuir fantasmas próximos impede o pacman reverter
            if(self.lastAction!= None):
                if (Directions.REVERSE[self.lastAction] in legal) and len(legal)>1:
                    legal.remove(Directions.REVERSE[self.lastAction])
        
        pacmanState = self.createState(state,legal) # Analisa o estado atual

        if pacmanState not in self.qValues: # Insere o estado na Q-Table
            self.initializeQValues(pacmanState, legal)

        if self.lastState != None: # Avalia a recompensa e atualiza Q-Table
            self.updateQValue(state,pacmanState)

        self.updateAttributes(state,pacmanState, legal) # Atualiza os atributos da classe

        self.incrementAcionsSoFar()

        return self.lastAction

    # Chamada no fim do episódio e atualiza o último estágio
    def final(self, state):
        legal = state.getLegalPacmanActions()

        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        
        if not self.ghostWasNear:
            if(self.lastAction!= None):
                if (Directions.REVERSE[self.lastAction] in legal) and len(legal)>1:
                    legal.remove(Directions.REVERSE[self.lastAction])

        if self.lastState != None:
            self.updateQValue(state,self.createState(state,legal), final_step=True)


        if(self.getNumTraining() < 2500):
            with open('episodesResults3.txt','a') as f:
                f.write(str(self.totalReward)+" "+str(self.getAcionsSoFar())+" "+str(state.getScore())+"\n")
        elif(self.getNumTraining() < 5500):
            with open('episodesResults2.txt','a') as f:
                f.write(str(self.totalReward)+" "+str(self.getAcionsSoFar())+" "+str(state.getScore())+"\n")
        else:
            with open('episodesResults1.txt','a') as f:
                f.write(str(self.totalReward)+" "+str(self.getAcionsSoFar())+" "+str(state.getScore())+"\n")

        self.resetAttributes()

        self.incrementEpisodesSoFar()

        if self.getEpisodesSoFar() == self.getNumTraining():
            self.setAlpha(0)
            self.setEpsilon(0)
