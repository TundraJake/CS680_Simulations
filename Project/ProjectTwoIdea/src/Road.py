'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Road
'''

import random as rand
import Patch

class Road(object):
	
	def __init__(self, numPatches):

		### Number Of Patches ###
		self.patches = []
		self.numPatches = numPatches
		self.totalArea = 0
		self.completePatches = 0

		# May start right on the first mile. 
		start = rand.randint(0, 2000)

		for i in range(numPatches):

			length = rand.randint(100, 3600)

			### Total Square feet
			self.patches.append(Patch.Patch(start, length))
			self.totalArea += self.patches[i].getArea()

			start += length

			# start has to be at least 100 feet from the previous patch. 
			start += rand.randint(100, 2000) 

	def getTotalPatchArea(self):
		return str(self.totalArea) + " Sqaure Feet"

	def getPatch(self, currentPatch):
		return self.patches[currentPatch]

	def incrementCompletedPatches(self):
		self.completePatches += 1

	def getNumPatches(self):
		return self.numPatches

	def getCompletedPatches(self):
		return self.completePatches
