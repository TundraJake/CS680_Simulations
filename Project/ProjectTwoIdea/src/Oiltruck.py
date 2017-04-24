'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Oiltruck
'''
import Vehicle
import random as rand

class Oiltruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.oil = 0
		self.patch = ''
		self.state = 0
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Spraying':2
				
				}

	def startWork(self, road):

		self.patch = road.getPatch(self.currentPatch)

		state = road.getPatch(self.currentPatch).getState()

		if (self.currentWorkTime == 0 and not self.busy and state == 'Graded'):
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.work()

	def work(self):
		if (self.currentWorkTime != 0):
			# print("Oiltruck working")
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			self.moveToNextPatch()
			self.patch.incrementState()
			return 0 

	def moveToNextPatch(self):
		self.currentPatch += 1

	def load(self):
		self.oil = 2000

	def layOil(self):
		self._oil -= 200



