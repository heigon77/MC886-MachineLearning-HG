from game import Agent
from game import Directions
from CrossOver import CrossOver
import numpy as np
from numpy.random import choice

class DumbAgent(Agent):
    "An agent that goes West until it can't." 

    def directions(self,state,p1=0,p2=0,p3=0,p4=0):
        "Get directions"

        co = CrossOver()

        if((p1+p2+p3+p4)!= 1):
            with open('results.txt','a') as f:
                string = str(co.agentNum) + "\n"
                f.write(string)

        dirs = [1, 2, 3, 4]
        randDir = choice(dirs, p=[p1,p2,p3,p4])
        
        if(randDir == 1):
            if (Directions.NORTH in state.getLegalPacmanActions()):
                return Directions.NORTH
            else:
                return Directions.STOP
        elif(randDir == 2):
            if (Directions.SOUTH in state.getLegalPacmanActions()):
                return Directions.SOUTH
            else:
                return Directions.STOP
        elif(randDir == 3):
            if (Directions.EAST in state.getLegalPacmanActions()):
                return Directions.EAST
            else:
                return Directions.STOP
        else:
            if (Directions.WEST in state.getLegalPacmanActions()):
                return Directions.WEST
            else:
                return Directions.STOP


    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."


        posG = np.array(state.getGhostPositions())
        posP = np.array(state.getPacmanPosition())

        if(np.linalg.norm(posG[0]-posP) < np.linalg.norm(posG[1]-posP)):
            distG = np.linalg.norm(posG[0]-posP)
            indG =  0
        else:
            distG = np.linalg.norm(posG[1]-posP)
            indG =  1

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

        
        if(len(state.getLegalPacmanActions()) == 2 ):
            path = "deadend"
        elif(len(state.getLegalPacmanActions()) == 3):
            if(Directions.SOUTH in state.getLegalPacmanActions() and Directions.NORTH in state.getLegalPacmanActions()):
                path = "corridorNS"
            elif(Directions.WEST in state.getLegalPacmanActions() and Directions.EAST in state.getLegalPacmanActions()):
                path = "corridorWE"
            elif(Directions.NORTH in state.getLegalPacmanActions() and Directions.EAST in state.getLegalPacmanActions()):
                path = "cornerNE"
            elif(Directions.NORTH in state.getLegalPacmanActions() and Directions.WEST in state.getLegalPacmanActions()):
                path = "cornerNW"
            elif(Directions.SOUTH in state.getLegalPacmanActions() and Directions.EAST in state.getLegalPacmanActions()):
                path = "cornerSE"
            else:
                path = "cornerSW"
        elif(len(state.getLegalPacmanActions()) == 4):
            if(Directions.SOUTH in state.getLegalPacmanActions() and Directions.NORTH in state.getLegalPacmanActions() and Directions.WEST in state.getLegalPacmanActions()):
                path = "TSNW"
            elif(Directions.SOUTH in state.getLegalPacmanActions() and Directions.NORTH in state.getLegalPacmanActions() and Directions.EAST in state.getLegalPacmanActions()):
                path = "TSNE"
            elif(Directions.SOUTH in state.getLegalPacmanActions() and Directions.EAST in state.getLegalPacmanActions() and Directions.WEST in state.getLegalPacmanActions()):
                path = "TSEW"
            else:
                path = "TNEW"
        else:
            path = "intersection"

        co = CrossOver()

        if(path == "deadend"):
            if (Directions.SOUTH in state.getLegalPacmanActions()):
                return Directions.SOUTH
            elif (Directions.NORTH in state.getLegalPacmanActions()):
                return Directions.NORTH
            elif (Directions.WEST in state.getLegalPacmanActions()):
                return Directions.WEST
            else:
                return Directions.EAST

        elif(distG < co.pmt[0]):
            if(path == "corridorNS"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[1],p2=co.pmt[2])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[3],p2=co.pmt[4])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[5],p2=co.pmt[6])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[7],p2=co.pmt[8])

                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[9],p2=co.pmt[10])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[11],p2=co.pmt[12])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[13],p2=co.pmt[14])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[15],p2=co.pmt[16])

            elif(path == "corridorWE"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p3=co.pmt[17],p4=co.pmt[18])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p3=co.pmt[19],p4=co.pmt[20])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p3=co.pmt[21],p4=co.pmt[22])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p3=co.pmt[23],p4=co.pmt[24])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p3=co.pmt[25],p4=co.pmt[26])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p3=co.pmt[27],p4=co.pmt[28])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p3=co.pmt[29],p4=co.pmt[30])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p3=co.pmt[31],p4=co.pmt[32])

            elif(path == "cornerNE"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[33],p3=co.pmt[34])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[35],p3=co.pmt[36])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[37],p3=co.pmt[38])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[39],p3=co.pmt[40])

                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[41],p3=co.pmt[42])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[43],p3=co.pmt[44])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[45],p3=co.pmt[46])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[47],p3=co.pmt[48])

            elif(path == "cornerNW"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[49],p4=co.pmt[50])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[51],p4=co.pmt[52])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[53],p4=co.pmt[54])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[55],p4=co.pmt[56])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[57],p4=co.pmt[58])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[59],p4=co.pmt[60])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[61],p4=co.pmt[62])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[63],p4=co.pmt[64])
            
            elif(path == "cornerSE"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p2=co.pmt[65],p3=co.pmt[66])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p2=co.pmt[67],p3=co.pmt[68])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p2=co.pmt[69],p3=co.pmt[70])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p2=co.pmt[71],p3=co.pmt[72])

                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p2=co.pmt[73],p3=co.pmt[74])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p2=co.pmt[75],p3=co.pmt[76])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p2=co.pmt[77],p3=co.pmt[78])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p2=co.pmt[79],p3=co.pmt[80])
            
            elif(path == "cornerSW"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p2=co.pmt[81],p4=co.pmt[82])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p2=co.pmt[83],p4=co.pmt[84])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p2=co.pmt[85],p4=co.pmt[86])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p2=co.pmt[87],p4=co.pmt[88])

                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p2=co.pmt[89],p4=co.pmt[90])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p2=co.pmt[91],p4=co.pmt[92])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p2=co.pmt[93],p4=co.pmt[94])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p2=co.pmt[95],p4=co.pmt[96])
            

            elif(path == "TSNW"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[97],p2=co.pmt[98],p4=co.pmt[99])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[100],p2=co.pmt[101],p4=co.pmt[102])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[103],p2=co.pmt[104],p4=co.pmt[105])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[106],p2=co.pmt[107],p4=co.pmt[108])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[109],p2=co.pmt[110],p4=co.pmt[111])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[112],p2=co.pmt[113],p4=co.pmt[114])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[115],p2=co.pmt[116],p4=co.pmt[117])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[118],p2=co.pmt[119],p4=co.pmt[120])
            
            elif(path == "TSNE"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[121],p2=co.pmt[122],p3=co.pmt[123])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[124],p2=co.pmt[125],p3=co.pmt[126])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[127],p2=co.pmt[128],p3=co.pmt[129])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[130],p2=co.pmt[131],p3=co.pmt[132])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[133],p2=co.pmt[134],p3=co.pmt[135])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[136],p2=co.pmt[137],p3=co.pmt[138])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[139],p2=co.pmt[140],p3=co.pmt[141])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[142],p2=co.pmt[143],p3=co.pmt[144])
            
            elif(path == "TSEW"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p2=co.pmt[145],p3=co.pmt[146],p4=co.pmt[147])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p2=co.pmt[148],p3=co.pmt[149],p4=co.pmt[150])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p2=co.pmt[151],p3=co.pmt[152],p4=co.pmt[153])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p2=co.pmt[154],p3=co.pmt[155],p4=co.pmt[156])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p2=co.pmt[157],p3=co.pmt[158],p4=co.pmt[159])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p2=co.pmt[160],p3=co.pmt[161],p4=co.pmt[162])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p2=co.pmt[163],p3=co.pmt[164],p4=co.pmt[165])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p2=co.pmt[166],p3=co.pmt[167],p4=co.pmt[168])
            
            elif(path == "TNEW"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[169],p3=co.pmt[170],p4=co.pmt[171])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[172],p3=co.pmt[173],p4=co.pmt[174])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[175],p3=co.pmt[176],p4=co.pmt[177])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[178],p3=co.pmt[179],p4=co.pmt[180])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[181],p3=co.pmt[182],p4=co.pmt[183])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[184],p3=co.pmt[185],p4=co.pmt[186])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[187],p3=co.pmt[188],p4=co.pmt[189])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[190],p3=co.pmt[191],p4=co.pmt[192])
            
            elif(path == "intersection"):
                if(ghostRelativePosition == "right"):
                    return self.directions(state=state,p1=co.pmt[193],p2=co.pmt[194],p3=co.pmt[195],p4=co.pmt[196])

                elif(ghostRelativePosition == "left"):
                    return self.directions(state=state,p1=co.pmt[197],p2=co.pmt[198],p3=co.pmt[199],p4=co.pmt[200])

                elif(ghostRelativePosition == "up"):
                    return self.directions(state=state,p1=co.pmt[201],p2=co.pmt[202],p3=co.pmt[203],p4=co.pmt[204])

                elif(ghostRelativePosition == "down"):
                    return self.directions(state=state,p1=co.pmt[205],p2=co.pmt[206],p3=co.pmt[207],p4=co.pmt[208])
                
                elif(ghostRelativePosition == "upright"):
                    return self.directions(state=state,p1=co.pmt[209],p2=co.pmt[210],p3=co.pmt[211],p4=co.pmt[212])

                elif(ghostRelativePosition == "upleft"):
                    return self.directions(state=state,p1=co.pmt[213],p2=co.pmt[214],p3=co.pmt[215],p4=co.pmt[216])

                elif(ghostRelativePosition == "downright"):
                    return self.directions(state=state,p1=co.pmt[217],p2=co.pmt[218],p3=co.pmt[219],p4=co.pmt[220])

                elif(ghostRelativePosition == "downleft"):
                    return self.directions(state=state,p1=co.pmt[221],p2=co.pmt[222],p3=co.pmt[223],p4=co.pmt[224])
        else:
            if(path == "corridorNS"):
                return self.directions(state=state,p1=co.pmt[225],p2=co.pmt[226])
            elif(path == "corridorWE"):
                return self.directions(state=state,p3=co.pmt[227],p4=co.pmt[228])
            elif(path == "cornerNE"):
                return self.directions(state=state,p1=co.pmt[229],p3=co.pmt[230])
            elif(path == "cornerNW"):
                return self.directions(state=state,p1=co.pmt[231],p4=co.pmt[232])
            elif(path == "cornerSE"):
                return self.directions(state=state,p2=co.pmt[233],p3=co.pmt[234])
            elif(path == "cornerSW"):
                return self.directions(state=state,p2=co.pmt[235],p4=co.pmt[236])
            elif(path == "TSNW"):
                return self.directions(state=state,p1=co.pmt[237],p2=co.pmt[238],p4=co.pmt[239])
            elif(path == "TSNE"):
                return self.directions(state=state,p1=co.pmt[240],p2=co.pmt[241],p3=co.pmt[242])
            elif(path == "TSEW"):
                return self.directions(state=state,p2=co.pmt[243],p3=co.pmt[244],p4=co.pmt[245])
            elif(path == "TNEW"):
                return self.directions(state=state,p1=co.pmt[246],p3=co.pmt[247],p4=co.pmt[248])
            elif(path == "intersection"):
                return self.directions(state=state,p1=co.pmt[249],p2=co.pmt[250],p3=co.pmt[251],p4=co.pmt[252])
            else:
                return Directions.STOP