'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
FEL class 
'''
from collections import deque

class FEL(object):

	def __init__(self):
		# 0th element = int type
		# 1st element = string type
		self.futureEventList = deque( [] ) 

	def pushEvent(self, time, person, action):
		listItem = [time, person, action]
		self.futureEventList.append(listItem)
		self.sortFEL()

	def printFEL(self):
		print(self.futureEventList)

	def sortFEL(self):
		unsort = sorted(self.futureEventList)
		self.futureEventList = deque(list(unsort))

	def popEvent(self):
		return self.futureEventList.popleft()

