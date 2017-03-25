'''
Jacob McKenna
UAF CS 680 Advanced Discrete Event Simulation 
Run File - Inits a simulation event of two servers and n customers.  
Many print functions may be uncommented to show bahavior of the simulation.
'''

# import Server
# import Simulation
import FEL

FEL = FEL.FEL()


FEL.pushEvent([3,4,5])
FEL.pushEvent([2,3,4])
FEL.pushEvent([1,2,3])
FEL.pushEvent([4])
FEL.pushEvent([5])
FEL.printFEL()
x = FEL.popEvent()
x = FEL.popEvent()
x = FEL.popEvent()

print(x)

# Simulation init func - 
# def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):

# sim1 = Simulation.Simulation(3,4, 3,5, 10000, 1,4)
# sim1.startSim("1")





