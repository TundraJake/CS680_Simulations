'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Stockpile
'''

import random as rand
from collections import deque

class Stockpile(object):

	def __init__(self, d1mat, location):
		self.d1mat = d1mat
		self.location = location # location is an int along a straight road
		self.queue = deque()

	def addD1Mat(self, truck):
		self.d1mat += truck.dump()

	def startLoading(self, truck):
		self.queue.append(truck)

	def loadDumpTruck(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()