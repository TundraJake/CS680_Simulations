'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Customer Class
'''

'''
Need refactor this into a better class, simulation is simulating
the customers. 
'''
import random as rd
from collections import deque
class Customers(object):

	def __init__(self, close, mint, maxt):
		self.arrivalTime = 0
		self.clockTimes = deque()
		self.custArrMin = mint
		self.custArrMax = maxt

		### Generates the customer arrival times.
		clock = 0 
		while clock < close:			
			time = rd.randint(self.custArrMin, self.custArrMax)
			clock += time 
			if clock < close:
				self.clockTimes.append(clock)


	### Debug Functions ###

	def printTimes(self):
		print(self.clockTimes)

	def getAllCustomers(self):
		return self.clockTimes

	def getCurrentCustomer(self, time):
		return self.clockTimes[time]

	def getLastCustomerTime(self):
		return self.clockTimes[-1]

