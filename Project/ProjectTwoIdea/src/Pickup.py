'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Pickup
'''

import Vehicle
import random as rand

class Pickup(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		super().__init__(employeeMinTime, employeeMaxTime, name)
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Marking':2

				}

	def work(self):
		if (self.currentWorkTime != 0):
			# print("Pickup working")
			self.currentWorkTime -= 1
			return 
			
		elif (self.currentWorkTime == 0 and self.busy): 
			self.toggleBusy()
			self.moveToNextPatch()
			self.patch.incrementState()
			return 0 

		else:
			return 0


	def changeState(self, newState):
		self.state = self.states[newState]