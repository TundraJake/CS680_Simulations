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

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Chipped'):
			# print("Pickup work")
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.work()

	def work(self):
		if (self.currentWorkTime != 0):
			# print("RubberTireRoller working")
			self.currentWorkTime -= 1
			self.utilTime += 1
			self.utilTime += 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy() # Not busy anymore.
			self.moveToNextPatch()
			self.patch.incrementState()
			self.road.incrementCompletedPatches()
			return 0 
