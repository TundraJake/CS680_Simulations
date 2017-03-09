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
		# 2nd element = event type
		self.futureEventList = deque( [] ) 

	def pushEvent(self, item):
		self.futureEventList.append(item)
		self.sortFEL()

	def printFEL(self):
		print(self.futureEventList)

	def sortFEL(self):
		unsort = sorted(self.futureEventList)
		self.futureEventList = deque(list(unsort))

	def popEvent(self):
		return self.futureEventList.popleft()

	def getFEL(self):
		return self.futureEventList
