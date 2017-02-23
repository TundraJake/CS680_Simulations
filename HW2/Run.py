'''
Jacob McKenna
UAF CS 680 Discrete Event SImulation 
Simulation Class and File
'''

import Server
import Simulation

'''
Customer and Sever Time Set One
''' 
### ### ### ### ### ### ### ### ### ### ### ### ### ###
### Construct these object in the simulation object ### 
### ### ### ### ### ### ### ### ### ### ### ### ### ###

# Simulation init func - 
# def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):

sim1 = Simulation.Simulation(1,5, 2,4, 100, 1,4)

sim1.startSim(20)


# server1 = Server.Server(1,5)

# server1.startService()
# server1.startService()

# #print(server1.getBusyState())

# server1.serveTheCustomer()
# server1.serveTheCustomer()
# server1.serveTheCustomer()
# server1.serveTheCustomer()
# server1.serveTheCustomer()
# server1.serveTheCustomer()



#sim2 = Simulation.Simulation(3,5, 1,3, 100, 4,7)

#sim3 = Simulation.Simulation(1,5, 2,4, 100, 1,10)

#sim4 = Simulation.Simulation(1,5, 2,4, 100, 1,2)



