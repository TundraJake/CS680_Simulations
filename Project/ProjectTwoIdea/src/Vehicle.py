'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Vehicle
'''

import random as rand


class Vehicle(object):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		self.busy = False
		self.name = name
		self.fuelTank = 0
		self.currentFuel = 0
		self.currentWorkTime = 0
		self.minTime = employeeMinTime
		self.maxTime = employeeMaxTime
		self.patchWorkTimes = []
		self.currentPatch = 0
		self.totalPatches = 0


	# def startWork(self):
	# 	if (self.currentWorkTime == 0 and not self.busy):
	# 		self.toggleBusy()
	# 		self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
	# 		self.patchWorkTimes.append(self.currentWorkTime)
	# 		self.work()

	# startWork = startWork

	def work(self):
		if (self.currentWorkTime != 0):
			self.currentWorkTime -= 1
			return 1
			
		elif (self.currentWorkTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			return 0

		else:
			return 0

	work = work

	def toggleBusy(self):
		self.busy = not self.busy

	def moveToNextPatch(self):
		if (self.totalPatches != self.currentPatch):
			self.currentPatch += 1	




















