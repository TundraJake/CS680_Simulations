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
					'Moving':1,
					'Loading':2,
					'Loaded':3,
					'Spraying':4
				
				}

		self.vehicleCostPerMinute = 1.72
		self.employeeCostPerMinute = 0.62 # Apprentice

		self.position = 0
		self.vehicleSpeed = 30 # mph 
		self.distanceRemaining = 0

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (not self.busy and self.patch.getState() == 'Graded'):
			# Needs a move fuction # self.position = self.patch.
			self.toggleBusy()
			# self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1

	def getTotalGallonsSprayed(self):
		return self.totalGallonsSprayed

	def refillOil(self):

		self.utilTime += 1
		self.oil += self.stockpile.loadDistributor()

		if(self.oil == 2500):
			self.changeState('Loaded')

	def moveToPit(self):

		self.distanceRemaining -= self.vehicleSpeed
		if (self.distanceRemaining < 0):
			self.changeState('Loading')
			self.refillOil()

	def spray(self):

		# self.currentWorkTime -= 1
		self.utilTime += 1
		oilAmount = 50
		self.oil -= oilAmount
		self.totalGallonsSprayed += oilAmount

		if (self.oil == 0): # 0, empty duh.
			self.changeState('Moving')
			self.distanceRemaining = self.patch.start - self.position

		else:

			if (self.patch.sprayPatch(oilAmount)):
				self.toggleBusy()
				self.moveToNextPatch()
				self.patch.incrementState()
				self.changeState('Moving')

	def work(self):

		if (self.busy):

			if (self.state == self.states['Loading']):
				self.refillOil()

			elif (self.state == self.states['Moving'] and self.oil == 0):
				self.moveToPit()
				# Needs a call move function. 

			elif (self.state == self.states['Moving']):
				self.changeState('Spraying')
				self.spray()
				# Needs a call move function. 

			
			elif(self.state == self.states['Spraying']):
				self.spray()

			elif(self.state == self.states['Loaded']):
				self.changeState('Moving')
				# self.currentWorkTime -= 1
				self.utilTime += 1

			self.appendState()


		else:
			self.appendState()



