'''
Jacob McKenna
UAF CS 680 Discrete Event SImulation 
Customer Class
'''

import random as rd

class Customers():

	def __init__(self, numCustomers, mint, maxt):
		self.arrivalTime = 0
		self.clockTimes = [] # FEL list for now, no proper FEL is in place yet.
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


	def printTimes(self):
		print(self.clockTimes)

	def getCurrentCustomer(self, time):
		return self.clockTimes[time]

	def getLastCustomerTime(self):
		return self.clockTimes[-1]

