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
custs = Customers.Customers(100, 1, 6)
server1 = Server.Server(1, 5)
server2 = Server.Server(2, 4)




