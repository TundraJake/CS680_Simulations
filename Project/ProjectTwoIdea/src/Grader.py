'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Grader
'''
import Vehicle
import random as rand

class Grader(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime):
		super().__init__(employeeMinTime, employeeMaxTime)
		self.patch = ''

	def startWork(self, road):

		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Grinded'):
			# print("GRADER STARTED")
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.work()

	def work(self):
		if (self.currentWorkTime != 0):
			# print("grader working")
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
