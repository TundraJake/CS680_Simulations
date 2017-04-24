'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation
Customer Class
'''

class Customer(object):

	def __init__(self, arrivalTime):
		self.arrivaltime = arrivaltime
		self.mainDeskWaitTime = 0
		self.secondDeskWaitTime = 0

	def setArrivalTime(self, arrivalTime):
		self.arrivaltime = arrivaltime

	def incrementMainDeskWaitTime(self):
		self.mainDeskWaitTime += 1

	def incrementSecondDeskWaitTime(self):
		self.secondDeskWaitTime += 1

	def getMainDeskWaitTime(self):
		return self.mainDeskWaitTime

	def getSecondDeskWaitTime(self):
		return self.secondDeskWaitTime