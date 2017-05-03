'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Dumptruck
'''
import Vehicle
import random as rand

class Dumptruck(Vehicle.Vehicle):

	def __init__(self, employeeMinTime, employeeMaxTime, name, stockpile, chipper):
		super().__init__(employeeMinTime, employeeMaxTime, name)

		self.stockpile = stockpile
		self.chipper = chipper 
		self.totalD1Hauled = 0
		self.d1 = 8 # cubic yards, starts full. 
		self.states = {
					
					'Parked':0,
					'Mobing':1,
					'Loading':2,
					'Loaded':3, 
					'Dumping':4
				
				}

		self.position = 0
		self.vehicleSpeed = 50 # fps ~ 40 mph 
		self.distanceRemaining = 0

	def startWork(self, road):

		self.road = road
		self.totalPatches = len(road.patches) - 1
		self.patch = road.getPatch(self.currentPatch)

		if (self.currentWorkTime == 0 and not self.busy and self.patch.getState() == 'Graded'):

			self.toggleBusy()
			# self.currentWorkTime = rand.randint(self.minTime, self.maxTime)
			self.patchWorkTimes.append(self.currentWorkTime)
			self.state = 1

	def getTotalD1Hauled(self):
		return self.totalD1Hauled

	def reloadD1(self):

		self.utilTime += 1
		self.d1 += self.stockpile.loadDumpTruck()
		print('im reloading', self.d1, self.name)
		if(self.d1 == 8):
			self.changeState('Loaded')


	def moveToPit(self):
		self.distanceRemaining -= self.vehicleSpeed
		if (self.distanceRemaining < 0):
			self.changeState('Loading')
			self.reloadD1()

	def dumping(self):

		self.currentWorkTime -= 1
		self.utilTime += 1
		d1Amount = .5


		if (self.d1 == 0): # 0, empty duh.
			self.changeState('Mobing')
			self.distanceRemaining = self.patch.start - self.position
			self.moveToPit()

		else:
			if(self.chipper.fillBin(d1Amount)):
				self.d1 -= d1Amount
				self.totalD1Hauled += d1Amount


	def work(self):

		if (self.busy):

			if (self.state == self.states['Loading']):
				self.reloadD1()

			elif (self.state == self.states['Mobing'] and self.d1 == 0):
				self.moveToPit()
				# Needs a call move function. 

			elif (self.state == self.states['Mobing']):
				self.changeState('Dumping')
				self.dumping()
				# Needs a call move function. 

			
			elif(self.state == self.states['Dumping']):
				self.dumping()

			elif(self.state == self.states['Loaded']):
				self.changeState('Mobing')
				# self.currentWorkTime -= 1
				self.utilTime += 1

			self.appendState()


		else:
			self.appendState()




