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
					'Moving':1,
					'Rolling':2
				
				}

		self.vehicleCostPerMinute = 4.5
		self.employeeCostPerMinute = .37

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Chipped'):

			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1

	def work(self):
		if (self.currentWorkTime != 0):

			if (self.state == self.states['Moving']):
				self.changeState('Rolling')
				self.currentWorkTime -= 1
				self.utilTime += 1
				# Needs a call move function. 
			
			elif(self.state == self.states['Rolling']):
				self.currentWorkTime -= 1
				self.utilTime += 1

			self.appendState()
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy()

			self.moveToNextPatch()
			self.patch.incrementState()
			self.road.incrementCompletedPatches()
			self.changeState('Moving')
			self.appendState()

		else:
			self.appendState()
			
		












