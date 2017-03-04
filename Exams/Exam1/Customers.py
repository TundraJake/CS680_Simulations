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

class Customers(object):

	def __init__(self, numCustomers, mint, maxt):
		self.arrivalTime = 0
		self.clockTimes = [] # FEL list for now, no proper FEL is in place yet.
		self.waitTimeForEachCustomer = []
		self.numCustomers = numCustomers
		self.custArrMin = mint
		self.custArrMax = maxt

		### Generates the customer arrival times.
		clock = 0 
		for _ in range(self.numCustomers):
			time = rd.randint(self.custArrMin, self.custArrMax)
			clock += time 
			self.clockTimes.append(clock)

	### Debug Functions ###

	def getAverageWaitTime(self):
		return 0

	def printTimes(self):
		print(self.clockTimes)

	def getAllCustomers(self):
		return self.clockTimes

	def getCurrentCustomer(self, time):
		return self.clockTimes[time]

	def getLastCustomerTime(self):
		return self.clockTimes[-1]

