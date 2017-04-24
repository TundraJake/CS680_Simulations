'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Dumptruck
'''
import Vehicle
import random as rand

class Dumptruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.__load = 0
		self.state = 0
		self.states = {
					
					'Hauling':0,
					'Loading':1,
					'Loaded':2, 
					'Dumping':3
				
				}

	def load(self):
		self.__load = 300

	def dump(self):
		return self.__load
