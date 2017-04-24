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

	def load(self):
		self.__load = 300

	def dump(self):
		return self.__load