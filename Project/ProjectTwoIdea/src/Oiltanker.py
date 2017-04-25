'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Oiltanker
'''

import random as rand
from collections import deque

class Oiltanker(object):

	def __init__(self, oil, location):
		self.oil = oil
		self.location = location # location is an int along a straight road
		self.tanker = ''

	def addD1Mat(self, truck):
		self.d1mat += truck.dump()

	def startLoading(self, truck):
		self.queue.append(truck)

	def loadDumpTruck(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()