'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Oiltruck
'''
import Vehicle
import random as rand

class Oiltruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name, stockpile):
		super().__init__(employeeMinTime, employeeMaxTime, name)
		self.stockpile = stockpile
		self.totalGallonsSprayed = 0
		self.oil = 2500 # Gallons, starts full.
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Loading':2,
					'Loaded':3,
					'Spraying':4
				
				}

		self.position = 0
		self.vehicleSpeed = 30 # mph 
		self.distanceRemaining = 0

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Graded'):

			self.toggleBusy()
			self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1


	def refillOil(self):

		self.utilTime += 1
		self.oil += 125
		print(self.oil, 'the fuck is this')

		if(self.oil == 2500):
			self.changeState('Loaded')

	def moveToPit(self):
		self.distanceRemaining -= self.vehicleSpeed
		if (self.distanceRemaining < 0):
			self.changeState('Loading')
			self.refillOil()

	def spray(self):

		self.currentWorkTime -= 1
		self.utilTime += 1
		oilAmount = 10
		self.oil -= oilAmount
		self.totalGallonsSprayed += oilAmount

		if (self.oil == 0): # 0, empty duh.
			self.changeState('Mobing')
			self.distanceRemaining = self.patch.start - self.position
			self.moveToPit()

		else:
			self.patch.sprayPatch(oilAmount)


	def work(self):

		if (self.currentWorkTime != 0):

			if (self.state == self.states['Loading']):
				self.refillOil()

			elif (self.state == self.states['Mobing'] and self.oil == 0):
				self.moveToPit()
				# Needs a call move function. 

			elif (self.state == self.states['Mobing']):
				self.changeState('Spraying')
				self.spray()
				# Needs a call move function. 

			
			elif(self.state == self.states['Spraying']):
				self.spray()

			elif(self.state == self.states['Loaded']):
				self.changeState('Mobing')
				self.currentWorkTime -= 1
				self.utilTime += 1

			self.appendState()

		elif (self.currentWorkTime == 0 and self.busy and self.currentPatch == self.totalPatches): 

			self.toggleBusy()

			self.moveToNextPatch()
			self.patch.incrementState()
			self.changeState('Parked')
			self.appendState()
			
		elif (self.currentWorkTime == 0 and self.busy): 

			self.toggleBusy()

			self.moveToNextPatch()
			self.patch.incrementState()
			self.changeState('Mobing')
			self.appendState()


		else:
			self.appendState()



