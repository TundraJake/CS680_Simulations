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
					'Moving':1,
					'Marking':2,
					'Fueling':3

				}
		self.vehicleCostPerMinute = 0.61
		self.employeeCostPerMinute = .37

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Damaged'):
			# print("Pickup work")
			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1
			

	def work(self):
		if (self.currentWorkTime != 0):

			if (self.state == self.states['Moving']):
				self.changeState('Marking')
				self.currentWorkTime -= 1
				self.utilTime += 1
				# Needs a call move function. 
			
			elif(self.state == self.states['Marking']):
				self.currentWorkTime -= 1
				self.utilTime += 1

			self.appendState()

		elif (self.currentWorkTime == 0 and self.busy and self.currentPatch == self.totalPatches): 

			self.toggleBusy()

			self.patch.incrementState()
			self.changeState('Fueling')
			self.appendState()
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy()

			self.moveToNextPatch()
			self.patch.incrementState()
			self.changeState('Moving')
			self.appendState()


		else:
			self.appendState()

	# def genUtilStats(self):
	# 	Parked = 0
	# 	Moving = 0
	# 	Marking = 0
	# 	Fueling = 0

	# 	for i in self.totalStateGraphList:

	# 		if (i == 0):
	# 			Parked += 1
	# 		elif (i == 1):
	# 			Moving += 1
	# 		elif (i == 2):
	# 			Marking += 1
	# 		elif (i == 3):
	# 			Fueling += 1

	# 	print(Parked, Moving  , Marking, Fueling,)



