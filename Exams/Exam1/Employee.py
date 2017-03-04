'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Employee Class
'''
import random as rand


''' Simulation controls the number of employees '''
class Employee(object):

	def __init__(self, name):
		self.name = name
		self.fulltime = rand.getrandbits(1)



