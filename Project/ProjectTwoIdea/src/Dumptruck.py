'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Dumptruck
'''
import Vehicle
import random as rand

class Dumptruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		super().__init__(employeeMinTime, employeeMaxTime, name)
		self.__load = 0
		self.state = 0
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Loading':2,
					'Loaded':3, 
					'Dumping':4
				
				}

	def load(self):
		self.__load = 300

	def dump(self):
		return self.__load
