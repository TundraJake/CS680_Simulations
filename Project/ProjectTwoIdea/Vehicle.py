'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: 
'''

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
		self.__busy = False

		self.__name = ''
		self.__fuelTank = 0
		self.__currentFuel = 0
		self.__currentWorkTime = 0

		self.__minTime = employeeMinTime
		self.__maxTime = employeeMaxTime

		self.__patchWorkTimes = []


	def startWork(self):
		if (self.__currentWorkTime == 0 and not self.__busy):
			self.toggleBusy()
			self.__currentWorkTime = rand.randint(self.__minTime, self.__maxTime)
			self.__patchWorkTimes.append(self.__currentWorkTime)


	def work(self):
		if (self.__currentWorkTime != 0):
			self.__currentWorkTime -= 1
			return 1
			# print("Server is busy.")

		elif (self.__currentWorkTime == 0 and self.__busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			return 0

		else:
			return 0

	def toggleBusy(self):
		self.__busy = not self.__busy
