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
		self.load = 0
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Loading':2,
					'Loaded':3, 
					'Dumping':4
				
				}

	def work(self):
		if (self.currentWorkTime != 0):
			# print("RubberTireRoller working")
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy() # Not busy anymore.
			self.moveToNextPatch()
			self.patch.incrementState()
			self.road.incrementCompletedPatches()
			return 0 

	def load(self):
		self.state = 2
		self.load = 300

	def dump(self):
		return self.__load
