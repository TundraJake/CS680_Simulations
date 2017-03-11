'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Run File - Inits a simulation event of two servers and n customers.  
Many print functions may be uncommented to show bahavior of the simulation.
'''

import Server
import Simulation
import MainDesk
import FEL

# Simulation init func - 

# def __init__(self, ctm, ctM, mdm, mdM, dlm, dlM, vrm, vrM, bom, boM, opens, closes, numDL, numVR, numBO):



m1 = MainDesk.MainDesk(1,4, 'MD')
s1 = Simulation.Simulation(1,4,   1,4,  10,20,   10,30  ,15,40, 480, 450,    2,2,1)
s1.startSim("Exam Sim One")


# myFEL = FEL.FEL()

# myFEL.pushEvent(5, 'c1', 'arrival')
# myFEL.pushEvent(5, 's1', 'start')


# myFEL.printFEL()


