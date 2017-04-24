'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Vehicle
'''

import random as rand

# VEHICLES ={
	
# 	# name 				: [Fuel Tank Amount, Cost Per Hour]
# 	'Dump Truck'		: [100.0, 75.50],
# 	'Rubber Tire Roller': [80.0, 60.50],
# 	'Steel Drum Roller'	: [80.0, 75.0],
# 	'M Grader'			: [80.0, 75.0],
# 	'Water Truck'		: [140.0, 75.0],
# 	'Chipper'			: [80.0, 89.50],

# 	'Ford F150 Pickup'	: [30.0, 53.0,],

# }


class Vehicle(object):

	def __init__(self, employeeMinTime, employeeMaxTime):
		self.busy = False
		self.name = ''
		self.fuelTank = 0
		self.currentFuel = 0
		self.currentWorkTime = 0
		self.minTime = employeeMinTime
		self.maxTime = employeeMaxTime
		self.patchWorkTimes = []
		self.currentPatch = 0


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























