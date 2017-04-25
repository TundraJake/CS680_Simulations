'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: RubberTireRoller
'''
import Vehicle
import random as rand

class RubberTireRoller(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		super().__init__(employeeMinTime, employeeMaxTime, name)
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Rolling':2
				
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
