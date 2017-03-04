'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Run File - Inits a simulation event of two servers and n customers.  
Many print functions may be uncommented to show bahavior of the simulation.
'''

import Server
#import Simulation
import MainDesk

# Simulation init func - 
# def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):

m1 = MainDesk.MainDesk(1,4)

m1.printServerTimes()