'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Ironwolf
'''
import Vehicle
import random as rand

class Ironwolf(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		super().__init__(employeeMinTime, employeeMaxTime, name)
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Grinding':2
				
				}

	def work(self):
		if (self.currentWorkTime != 0):
			# print("iron wolf working")
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			self.moveToNextPatch()
			self.patch.incrementState()
			return 0 
			
		else:
			return 0
	
