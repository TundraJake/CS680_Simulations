'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Sumulation
'''
import os
import time # Used for the clock (seconds).
import random as rand
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import Image

from collections import deque

# Road
import Road
import Patch

# Vehicles
import time
import Pickup
import Ironwolf
import Grader
import Oiltruck
import Chipper
import RubberTireRoller
import Dumptruck

# Stockpile 
import Stockpile

class Simulation(object):

	def __init__(self, budget, patches, numDumpTrucks, numOilTrucks):

		self.simClock = 0
		self.totalSimTime = 0 
		self.budget = budget
		self.timePoints = []

		###### Cubic Feet, Gallons, int Location ######
		self.stockpile = Stockpile.Stockpile(1000, 11600, 0)

		self.road = Road.Road(patches)

		self.chipper = Chipper.Chipper(30,40, 'Chipper')

		self.flaggerOne = Pickup.Pickup(5,8, 'Pickup')
		self.flaggerTwo = Pickup.Pickup(5,8, 'Pickup')
		self.pilotCar = Pickup.Pickup(5,8, 'Pickup')

		self.numDumpTrucks = []
		for i in range(numDumpTrucks):
			self.numDumpTrucks.append(Dumptruck.Dumptruck(10,20,'Dumptruck ' + str(i + 1), self.stockpile, self.chipper))

		self.numOilTrucks = []
		for i in range(numOilTrucks):
			self.numOilTrucks.append(Oiltruck.Oiltruck(30,40,'Distributor '+str(i + 1), self.stockpile))

		self.pickup = Pickup.Pickup(5,8, 'Pickup')
		self.ironwolf = Ironwolf.Ironwolf(10,30, 'Ironwolf')
		self.grader = Grader.Grader(40,80, 'Grader')

		self.rtr = RubberTireRoller.RubberTireRoller(15,30, 'RTR')

		self.oilArrivalTime = 0
		self.day = 1

		self.oilDeliveryTime = 0
		self.d1DeliveryTime = 0 

		self.costPerDayList = []


	def timeUntilRefill(self):
		oilfirst = 1
		oilsecond = 3

		d1first = 1
		d1second = 2 

		if (self.oilDeliveryTime == 0):
			self.oilDeliveryTime = rand.randint(oilfirst, oilsecond)

		if (self.d1DeliveryTime == 0):
			self.d1DeliveryTime = rand.randint(d1first, d1second)

		if (self.d1DeliveryTime > 0):
			
			self.d1DeliveryTime -= 1
			
			if (self.d1DeliveryTime == 0):
				self.refillD1Pit()

		if (self.oilDeliveryTime > 0):
			
			self.oilDeliveryTime -= 1
			
			if (self.oilDeliveryTime == 0):
				self.refillOilTanker()


	def refillOilTanker(self):
		self.stockpile.addOil()

	def refillD1Pit(self):
		self.stockpile.addD1Mat()


	def vehicleStartWork(self):

		if (not self.pilotCar.busy):
			self.flaggerOne
		if (not self.pilotCar.busy):
			self.flaggerTwo
		if (not self.pilotCar.busy):
			self.pilotCar  

		if (not self.pickup.busy):
			self.pickup.startWork(self.road)

		if (not self.ironwolf.busy):
			self.ironwolf.startWork(self.road)
		
		if (not self.grader.busy):
			self.grader.startWork(self.road)

		for i in range(len(self.numOilTrucks)):
			if (not self.numOilTrucks[i].busy):
				self.numOilTrucks[i].startWork(self.road)

		for i in range(len(self.numDumpTrucks)):
			if (not self.numDumpTrucks[i].busy):
				self.numDumpTrucks[i].startWork(self.road)

		if (not self.chipper.busy):
			self.chipper.startWork(self.road)

		if (not self.rtr.busy):
			self.rtr.startWork(self.road)

	def checkWork(self):

		self.flaggerOne.work()
		self.flaggerTwo.work()
		self.pilotCar.work()
		
		self.pickup.work()
		self.grader.work()
		self.ironwolf.work()
	
		for i in range(len(self.numOilTrucks)):
			self.numOilTrucks[i].work()

		for i in range(len(self.numDumpTrucks)):
			self.numDumpTrucks[i].work()

		self.chipper.work()
		self.rtr.work()
	
	def genGraphs(self, simName):

		########### Vehicle Utilization Graphs #############

		self.pickup.genUtilGraphs(simName, self.day)
		self.grader.genUtilGraphs(simName, self.day)
		self.ironwolf.genUtilGraphs(simName, self.day)

		for i in self.numOilTrucks:
			i.genUtilGraphs(simName, self.day)

		for i in self.numDumpTrucks:
			i.genUtilGraphs(simName, self.day)

		self.chipper.genUtilGraphs(simName, self.day)
		self.rtr.genUtilGraphs(simName, self.day)

		########### Vehicle State Graphs #############

		self.pickup.genStateGraphs(simName,self.timePoints, self.day)
		self.grader.genStateGraphs(simName,self.timePoints, self.day)
		self.ironwolf.genStateGraphs(simName,self.timePoints, self.day)

		for i in self.numOilTrucks:
			i.genStateGraphs(simName,self.timePoints, self.day)

		for i in self.numDumpTrucks:
			i.genStateGraphs(simName,self.timePoints, self.day)

		self.chipper.genStateGraphs(simName,self.timePoints, self.day)
		self.rtr.genStateGraphs(simName,self.timePoints, self.day)

		############# Resource Stockpile Graphs #############

		self.stockpile.genD1matGraph(simName, self.day)
		self.stockpile.getOilmatGraph(simName, self.day)

	def totalAllVehicleCosts(self):

		vehicleTotal = 0

		vehicleTotal += self.flaggerOne.getVehicleCosts()
		vehicleTotal += self.flaggerTwo.getVehicleCosts()
		vehicleTotal += self.pilotCar.getVehicleCosts()

		vehicleTotal += self.pickup.getVehicleCosts()
		vehicleTotal += self.grader.getVehicleCosts()
		vehicleTotal += self.ironwolf.getVehicleCosts()

		for i in self.numOilTrucks:
			vehicleTotal += i.getVehicleCosts()

		for i in self.numDumpTrucks:
			vehicleTotal += i.getVehicleCosts()

		vehicleTotal += self.chipper.getVehicleCosts()
		vehicleTotal += self.rtr.getVehicleCosts()

		return vehicleTotal

	def totalAllEmployeeCosts(self):

		employeeTotal = 0

		employeeTotal += self.flaggerOne.getEmployeeCosts()
		employeeTotal += self.flaggerTwo.getEmployeeCosts()
		employeeTotal += self.pilotCar.getEmployeeCosts()

		employeeTotal += self.pickup.getEmployeeCosts()
		employeeTotal += self.grader.getEmployeeCosts()
		employeeTotal += self.ironwolf.getEmployeeCosts()

		for i in self.numOilTrucks:
			employeeTotal += i.getEmployeeCosts()

		for i in self.numDumpTrucks:
			employeeTotal += i.getEmployeeCosts()

		employeeTotal += self.chipper.getEmployeeCosts()
		employeeTotal += self.rtr.getEmployeeCosts()

		return employeeTotal

	def getOilCosts(self):
		total = 0

		for i in self.numOilTrucks:
			print(i.getTotalGallonsSprayed(), 'Gallons of Oil Distributed from ' + i.getName())
			total += i.getTotalGallonsSprayed()


		total = total * 10.4 # $10.40 a Gallon of oil	
		total += self.stockpile.getOilDeliveryCost()
		return total
	
	def getD1Costs(self):
		total = 0

		for i in self.numDumpTrucks:
			print(i.getTotalD1Hauled(), 'Cubic Yards pf D1 Hauled from ' + i.getName())
			total += i.getTotalD1Hauled()


		total = total * 17.5 # $17.5 a cubic yard
		total += self.stockpile.getD1DeliveryCost()
		return total

	def getAllCosts(self):

		total = 0

		total += self.totalAllVehicleCosts()
		total += self.totalAllEmployeeCosts()
		total += self.getOilCosts()
		total += self.getD1Costs()

		return total 

	def incrementUtil(self):

		self.flaggerOne.genUtilTime(self.simClock)
		self.flaggerTwo.genUtilTime(self.simClock)
		self.pilotCar.genUtilTime(self.simClock)

		self.pickup.genUtilTime(self.simClock)
		self.grader.genUtilTime(self.simClock)
		self.ironwolf.genUtilTime(self.simClock)

		for i in self.numOilTrucks:
			i.genUtilTime(self.simClock)

		for i in self.numDumpTrucks:
			i.genUtilTime(self.simClock)

		self.chipper.genUtilTime(self.simClock)
		self.rtr.genUtilTime(self.simClock)

		###### Stockpile #####

		self.stockpile.appendResourceNodes()

	def getUtilStats(self):
		self.pickup.genUtilStats()

	def startSim(self, simName):

		myIter = 0 
		
		while self.road.getCompletedPatches() != self.road.getNumPatches():

			self.vehicleStartWork()
			self.checkWork()

			# print(self.road.getCompletedPatches() )
			# print(self.simClock)
			# print(self.road.patches[0].getState(), " patch 1")
			# print(self.road.patches[1].getState(), " patch 2")
			# print(self.road.patches[2].getState(), " patch 3")
			# print(self.road.patches[3].getState(), " patch 4")
			# print(self.road.patches[49].getState(), " patch 5")

			# print(self.road.getCompletedPatches())

			# time.sleep(.00001)
			self.simClock += 1
			self.timePoints.append(self.simClock)
			self.incrementUtil()

			if((self.simClock % 720) == 0):
				print('Day', self.day, ' graphs')
				self.totalSimTime += self.simClock
				# self.genGraphs(simName)
				self.simClock = 0 # Reset Day
				self.timePoints = []
				self.timeUntilRefill()

				self.day += 1

		
		# directory = '../sims/' + simName + '/graphs'
		

		# if not os.path.exists(directory + simName):
		# 	os.makedirs(directory + '/util/')
		# 	os.makedirs(directory + '/state/')
		# 	os.makedirs(directory + '/resources/')

		self.getUtilStats()

		print(self.totalSimTime, "Total Time (minutes)")
		projectCost = self.getAllCosts()
		if(projectCost < self.budget):
			print('Project within Budget!\nProject Cost:', projectCost,
				'\nMoney Saved: ', self.budget - projectCost)
		else:
			print('Project out of Budget!\nProject Cost:', projectCost,
				'\nOver Budget Amount: ', projectCost - self.budget)


		print(self.road.getTotalPatchArea(), ' sqaure feet of patches')




s = Simulation(5000000, 50, 3, 1)
s.startSim("Test_Sim4")

# s = Simulation(5000000, 200, 3, 1)
# s.startSim("Test_Sim2")







