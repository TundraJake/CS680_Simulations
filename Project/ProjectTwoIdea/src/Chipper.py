
'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Chipper
'''
import Vehicle
import random as rand

class Chipper(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		super().__init__(employeeMinTime, employeeMaxTime, name)

		self.d1InBin = 0 # Starts empty, 1 cubic yard max. 
		self.totalLayedD1 = 0
		self.states = {
					
					'Parked':0,
					'Moving':1,
					'Chipping':2
				
				}

		self.vehicleCostPerMinute = 1.45
		self.employeeCostPerMinute = 2 *.57

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (not self.busy and self.patch.getState() == 'Oiled'):

			self.toggleBusy()
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1
			
	def fillBin(self, d1):
		if(self.d1InBin <= 1):
			self.d1InBin += d1
			return 1
		else:
			return 0


	def chip(self):

		if(self.d1InBin == 0):
			self.changeState('Parked')

		else:
			self.utilTime += 1
			d1Amount = .5
			self.totalLayedD1 += d1Amount
			result = self.patch.chipPatch(d1Amount)
			self.d1InBin -= d1Amount
			self.changeState('Chipping')

			if(result):
				self.toggleBusy()
				self.moveToNextPatch()
				self.patch.incrementState()
				self.changeState('Moving')

	def work(self):
		if (self.busy):

			if (self.state == self.states['Moving']):

				self.changeState('Chipping')
				self.chip()
				# Needs a call move function. 
			
			elif(self.state == self.states['Chipping']):
				# print('sthjiaergonuethaigornus')
				self.chip()

			elif(self.state == self.states['Parked']):
				self.chip() # Try to go back to chipping.

			self.appendState()



		else:
			# print('sthjiaergonuethaigornus')
			self.appendState()
	