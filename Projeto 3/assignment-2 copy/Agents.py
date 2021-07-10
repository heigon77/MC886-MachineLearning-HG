from game import Agent
from game import Directions
from ReadWrite import ReadWrite
import numpy as np
from numpy.random import choice

class DumbAgent(Agent):
    "An agent that is learning." 

    numCaps = None
    GhostVulnerable = False
    Attack = None
    PreviusMove = None

    PossibleDirections = [
        [1,2,3,4], 
        [1,2,4,3], 
        [1,3,2,4], 
        [1,3,4,2], 
        [1,4,2,3], 
        [1,4,3,2], 
        [2,1,3,4], 
        [2,1,4,3], 
        [2,3,1,4], 
        [2,3,4,1],
        [2,4,1,3],
        [2,4,3,1],
        [3,1,2,4],
        [3,1,4,2],
        [3,2,1,4],
        [3,2,4,1],
        [3,4,1,2],
        [3,4,2,1],
        [4,1,2,3],
        [4,1,3,2],
        [4,2,1,3],
        [4,2,3,1],
        [4,3,1,2],
        [4,3,2,1],
    ]

    def numberToDirection(self,number):
        if(number == 1):
            return Directions.NORTH
        elif(number == 2):
            return Directions.SOUTH
        elif(number == 3):
            return Directions.EAST
        else:
            return Directions.WEST

    def directionsProb(self,state,p1=0,p2=0,p3=0,p4=0):
        "Get directions based on probability"

        dirs = [1, 2, 3, 4]
        randDir = choice(dirs, p=[p1,p2,p3,p4])
        
        if(randDir == 1):
            if (Directions.NORTH in state.getLegalPacmanActions()):
                self.PreviusMove = Directions.NORTH
                return Directions.NORTH
            else:
                if(self.PreviusMove in state.getLegalPacmanActions()):
                    return self.PreviusMove
                else:
                    return Directions.STOP
        elif(randDir == 2):
            if (Directions.SOUTH in state.getLegalPacmanActions()):
                self.PreviusMove = Directions.SOUTH
                return Directions.SOUTH
            else:
                if(self.PreviusMove in state.getLegalPacmanActions()):
                    return self.PreviusMove
                else:
                    return Directions.STOP
        elif(randDir == 3):
            if (Directions.EAST in state.getLegalPacmanActions()):
                self.PreviusMove = Directions.EAST
                return Directions.EAST
            else:
                if(self.PreviusMove in state.getLegalPacmanActions()):
                    return self.PreviusMove
                else:
                    return Directions.STOP
        else:
            if (Directions.WEST in state.getLegalPacmanActions()):
                self.PreviusMove = Directions.WEST
                return Directions.WEST
            else:
                if(self.PreviusMove in state.getLegalPacmanActions()):
                    return self.PreviusMove
                else:
                    return Directions.STOP
        
    def directions(self,state,seq):
        "Get directions based on a possible sequence"

        fst = self.numberToDirection(seq[0])
        sec = self.numberToDirection(seq[1])
        trh = self.numberToDirection(seq[2])
        fth = self.numberToDirection(seq[3])

        if (fst in state.getLegalPacmanActions()):
            return fst
        elif (sec in state.getLegalPacmanActions()):
            return sec
        elif (trh in state.getLegalPacmanActions()):
            return trh
        else:
            fth

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."

        rw = ReadWrite()
        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())
        posCaps = np.array(state.getCapsules())
        posFood = state.getFood()
        
        if(self.numCaps == None):
            self.numCaps = len(posCaps)
        elif(self.numCaps != len(posCaps)):
            self.numCaps = len(posCaps)
            self.Attack = 0
        elif(self.Attack >= rw.pmt[1]):
            self.Attack = None

        if(self.Attack != None):
            self.Attack += 1

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

        if(len(state.getLegalPacmanActions()) == 2 ):
            path = "deadend"
        else:
            path = None

        if(path == "deadend"):
            if (Directions.SOUTH in state.getLegalPacmanActions()):
                return Directions.SOUTH
            elif (Directions.NORTH in state.getLegalPacmanActions()):
                return Directions.NORTH
            elif (Directions.WEST in state.getLegalPacmanActions()):
                return Directions.WEST
            else:
                return Directions.EAST

        elif(minDistGhost < rw.pmt[0] and self.Attack == None):
            if(ghostRelativePosition == "right"):
                return self.directions(state,self.PossibleDirections[rw.pmt[2]])

            elif(ghostRelativePosition == "left"):
                return self.directions(state,self.PossibleDirections[rw.pmt[3]])

            elif(ghostRelativePosition == "up"):
                return self.directions(state,self.PossibleDirections[rw.pmt[4]])

            elif(ghostRelativePosition == "down"):
                return self.directions(state,self.PossibleDirections[rw.pmt[5]])

            elif(ghostRelativePosition == "downright"):
                return self.directions(state,self.PossibleDirections[rw.pmt[6]])

            elif(ghostRelativePosition == "downleft"):
                return self.directions(state,self.PossibleDirections[rw.pmt[7]])
            
            elif(ghostRelativePosition == "upleft"):
                return self.directions(state,self.PossibleDirections[rw.pmt[8]])
            
            elif(ghostRelativePosition == "upright"):
                return self.directions(state,self.PossibleDirections[rw.pmt[9]])
        else:
            if(foodRelativePosition == "right"):
                return self.directionsProb(state=state,p1=rw.pmt[10],p2=rw.pmt[11],p3=rw.pmt[12],p4=rw.pmt[13])

            elif(foodRelativePosition == "left"):
                return self.directionsProb(state=state,p1=rw.pmt[14],p2=rw.pmt[15],p3=rw.pmt[16],p4=rw.pmt[17])

            elif(foodRelativePosition == "up"):
                return self.directionsProb(state=state,p1=rw.pmt[18],p2=rw.pmt[19],p3=rw.pmt[20],p4=rw.pmt[21])

            elif(foodRelativePosition == "down"):
                return self.directionsProb(state=state,p1=rw.pmt[22],p2=rw.pmt[23],p3=rw.pmt[24],p4=rw.pmt[25])

            elif(foodRelativePosition == "downright"):
                return self.directionsProb(state=state,p1=rw.pmt[26],p2=rw.pmt[27],p3=rw.pmt[28],p4=rw.pmt[29])

            elif(foodRelativePosition == "downleft"):
                return self.directionsProb(state=state,p1=rw.pmt[30],p2=rw.pmt[31],p3=rw.pmt[32],p4=rw.pmt[33])
            
            elif(foodRelativePosition == "upleft"):
                return self.directionsProb(state=state,p1=rw.pmt[34],p2=rw.pmt[35],p3=rw.pmt[36],p4=rw.pmt[37])
            
            elif(foodRelativePosition == "upright"):
                return self.directionsProb(state=state,p1=rw.pmt[38],p2=rw.pmt[39],p3=rw.pmt[40],p4=rw.pmt[41])

    def final(self, state):
        posCaps = np.array(state.getCapsules())
        print ("Acabou",posCaps)
