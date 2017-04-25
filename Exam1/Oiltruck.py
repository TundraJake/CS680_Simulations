'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Dumptruck
'''

import Vehicle

class Oiltruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.__oil = 0 # gallons

	def load(self):
		self.__oil = 2000

	def layOil(self):
		self._oil -= 200
