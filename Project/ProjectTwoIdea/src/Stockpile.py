'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Stockpile - Both Oil and D1
'''

import random as rand
from collections import deque

class Stockpile(object):

	def __init__(self, d1mat, oil,location):

		self.d1mat = d1mat
		self.oilTanker = oil


		self.location = location # location is an int along a straight road
		self.queue = deque()


	def addD1Mat(self, truck):
		self.d1mat += truck.unload()

	def addOil(self, tanker):
		self.oilTanker += tanker.unload()


	def loadDumpTruck(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()

	def loadDistributor(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()


	def startLoadingOil(self, truck):
		self.queue.append(truck)

	def startLoading(self, truck):
		self.queue.append(truck)