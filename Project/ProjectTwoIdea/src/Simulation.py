'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Sumulation
'''

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

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation(object):

	def __init__(self, budget, patches, numDumpTrucks, numOilTrucks):

		self.simClock = 0
		self.budget = budget
		self.timePoints = []

		self.road = Road.Road(patches)

		self.numDumpTrucks = []
		for i in range(numDumpTrucks):
			self.numDumpTrucks.append(Dumptruck.Dumptruck(10,20,'Dumptruck' + str(i + 1)))

		self.numOilTrucks = []
		for i in range(numOilTrucks):
			self.numOilTrucks.append(Oiltruck.Oiltruck(30,40,'Oil '+str(i + 1)))

		self.pickup = Pickup.Pickup(3,6, 'Pickup')
		self.ironwolf = Ironwolf.Ironwolf(10,30, 'Ironwolf')
		self.grader = Grader.Grader(40,80, 'Grader')
		self.chipper = Chipper.Chipper(30,40, 'Chipper')
		self.rtr = RubberTireRoller.RubberTireRoller(15,30, 'RTR')

	def vehicleStartWork(self):

		if (not self.pickup.busy):
			self.pickup.startWork(self.road)

		if (not self.ironwolf.busy):
			self.ironwolf.startWork(self.road)
		
		if (not self.grader.busy):
			self.grader.startWork(self.road)

		for i in range(len(self.numOilTrucks)):
			if (not self.numOilTrucks[i].busy):
				self.numOilTrucks[i].startWork(self.road)

		if (not self.chipper.busy):
			self.chipper.startWork(self.road)

		if (not self.rtr.busy):
			self.rtr.startWork(self.road)

	def checkWork(self):
		self.pickup.work()
		self.grader.work()
		self.ironwolf.work()
	
		for i in range(len(self.numOilTrucks)):
			self.numOilTrucks[i].work()

		self.chipper.work()
		self.rtr.work()
	
	def startSim(self, name):

		# print(self.arrivalTimes) # Testing times, functions correctly. 
		myIter = 0 
		

		while self.road.getCompletedPatches() != self.road.getNumPatches():

			self.vehicleStartWork()
			self.checkWork()

			# print(self.road.patches[0].getState(), " patch 1")
			# print(self.road.patches[1].getState(), " patch 2")
			# print(self.road.patches[2].getState(), " patch 3")
			# print(self.road.patches[3].getState(), " patch 4")
			# print(self.road.patches[4].getState(), " patch 5")

			print(self.road.getCompletedPatches())


			time.sleep(.0001)
			self.simClock += 1
		print(self.simClock, "Total Time")

s = Simulation(5000000, 100, 3, 1)
s.startSim("test sim")






