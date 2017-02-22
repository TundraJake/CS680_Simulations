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
		self.custArrivals = numCustomers
		self.custArrMin = mint
		self.custArrMax = maxt

		clock = 0 
		for _ in range(self.custArrivals):
			time = rd.randint(self.custArrMin, self.custArrMax)
			clock += time 
			self.clockTimes.append(clock)


	### Debug Functions ###

	def printTimes(self):
		print(self.clockTimes)

	def getLastCustomerTime(self):
		return self.clockTimes[-1]

