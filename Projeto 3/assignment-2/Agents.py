from game import Agent
from game import Directions
from CrossOver import CrossOver
import numpy as np

class DumbAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."

        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())
        posCaps = np.array(state.getCapsules())
        walls = state.getWalls()

        distG = min(np.linalg.norm(posG[0]-posP),np.linalg.norm(posG[1]-posP))

        co = CrossOver()

        distCaps = co.distCap

        if(len(posCaps)>0):
            for i in posCaps:
                distCaps = min(distCaps,np.linalg.norm(i-posP))

        # print("Ghost Positions:")
        # print(posG)
        # print("Pacman Position:")
        # print(posP)
        # print("Distance closest ghost:")
        # print(distG)
        # print("Positions Capsules:")
        # print(posCaps)
        # print("Distance closest capsule")
        # print(distCaps)
        # print("Num value:")
        # print(co.agentNum)

        if(distG < co.num5 and walls[posP[0]-1][posP[1]]==False):
            if Directions.WEST in state.getLegalPacmanActions():
                return Directions.WEST
            else:
                return Directions.STOP

        elif(distCaps < co.num3 and walls[posP[0]][posP[1]+1]==False):
            if Directions.NORTH in state.getLegalPacmanActions():
                return Directions.NORTH
            else:
                return Directions.STOP

        elif(distG > co.num7 and walls[posP[0]+1][posP[1]]==False):
            if Directions.EAST in state.getLegalPacmanActions():
                return Directions.EAST
            else:
                return Directions.STOP

        else:
            if (Directions.EAST in state.getLegalPacmanActions()):
                return Directions.EAST
            elif (Directions.SOUTH in state.getLegalPacmanActions()):
                return Directions.SOUTH
            elif (Directions.WEST in state.getLegalPacmanActions()):
                return Directions.WEST
            else:
                return Directions.NORTH