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

			if (self.state == self.states['Mobing']):
				self.changeState('Marking')
				self.appendState()
				self.currentWorkTime -= 1
				self.utilTime += 1
				# Needs a call move function. 


			
			elif(self.state == self.states['Marking']):
				self.appendState()
				self.currentWorkTime -= 1
				self.utilTime += 1


			# # print("Pickup working")
			# self.currentWorkTime -= 1
			# self.utilTime += 1
			

			
		elif (self.currentWorkTime == 0 and self.busy): 
			self.toggleBusy()
			self.moveToNextPatch()
			self.patch.incrementState()
			self.appendState()


		else:
			self.appendState()
