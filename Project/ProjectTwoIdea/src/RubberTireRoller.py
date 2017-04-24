'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: RubberTireRoller
'''
import Vehicle
import random as rand

class RubberTireRoller(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.patch = ''
		self.state = 0
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Rolling':2
				
				}

	def startWork(self, road):

		self.patch = road.getPatch(self.currentPatch)

		state = road.getPatch(self.currentPatch).getState()

		if (self.currentWorkTime == 0 and not self.busy and state == 'Chipped'):
			print("RubberTireRoller started working")
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.work()

	def work(self):
		if (self.currentWorkTime != 0):
			print("RubberTireRoller working")
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy() # Not busy anymore.
			self.moveToNextPatch()
			self.patch.incrementState()
			return 0 

	def moveToNextPatch(self):

		self.currentPatch += 1