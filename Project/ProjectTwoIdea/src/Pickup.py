'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Pickup
'''

import Vehicle
import random as rand

class Pickup(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.patch = ''
		self.state = 0
		self.states = {
					
					'Parked':0,
					'Marking':1
					
				}

	def startWork(self, road):

		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Damaged'):
			# print("Pickup work")
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.work()

	def work(self):
		if (self.currentWorkTime != 0):
			# print("Pickup working")
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 
			self.toggleBusy()
			self.moveToNextPatch()
			self.patch.incrementState()
			return 0 

	def moveToNextPatch(self):
		if 
		self.currentPatch += 1