'''
Jacob McKenna
UAF CS 680 Discrete Event SImulation 
Simulation Class and File
'''

import Server
import Simulation
import Customers

'''
Customer and Sever Time Set One
''' 
### ### ### ### ### ### ### ### ### ### ### ### ### ###
### Construct these object in the simulation object ### 
### ### ### ### ### ### ### ### ### ### ### ### ### ###

# Simulation init func - 
# def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):
s1 = Simulation.Simulation(1,5, 2,4, 100,1,4)

s2 = Simulation.Simulation(3,5, 1,3, 100,4,7)

s3 = Simulation.Simulation(1,5, 2,4, 100,1,10)

s4 = Simulation.Simulation(1,5, 2,4, 100,1,2)



