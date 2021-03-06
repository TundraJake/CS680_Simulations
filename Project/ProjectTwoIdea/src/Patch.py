'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Patch
'''
import math

class Patch(object):

	def __init__(self, start, length):
		self.start = start
		self.width = 30 # 30 feet
		self.length = length
		self.end = start + length
		self.area = self.width * self.length
		self.state = 0
		self.requiredOil = math.floor(0.016 * self.area) # gallons convers
		self.requiredD1 = math.floor(0.001 * self.area) # cubic yards convers
		self.states = {
					
					0:'Damaged',
					1:'Marked',
					2:'Grinded',
					3:'Graded',
					4:'Oiled',
					5:'Chipped',
					6:'Rolled-Finished'
				
				}

	def getState(self):
		return self.states[self.state]

	def setState(self, state):
		self.state = state

	def incrementState(self):
		self.state += 1
		
		# if self.getState() == self.states[6]:
		# 	return "Finished Patch"

	def getArea(self):
		return self.area

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	# Debug function
	def printStartAndEnd(self):
		print('Start is: ', self.start, ' and end is: ', self.end)

	def printRemainingGallonsToFinish(self):
		print(self.requiredOil, ' gallons of oil left to cover the patch.')

	def sprayPatch(self, oil):
		self.requiredOil -= oil

		if (self.requiredOil < 0):
			return 1

		else:
			return 0




	def chipPatch(self, d1):
		self.requiredD1 -= d1

		if (self.requiredD1 < 0):
			return 1

		else:
			return 0

