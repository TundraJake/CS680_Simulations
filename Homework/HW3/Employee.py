'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Employee Class
'''
import random as rand
import numpy as np
'''
Stretch Goal - set employee poor and high quality employees,
the rate at which they operate on average times. 
Also add sick or healthy status.
'''

''' Simulation controls the number of employees '''
class Employee(object):

	def __init__(self, name):
		self.name = name
		self.fulltime = rand.getrandbits(1)



