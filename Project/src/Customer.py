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

class Customer(object):

	def __init__(self, close, mint, maxt):
		self.arrivalTime = 0
		self.clockTimes = deque()
		self.custArrMin = mint
		self.custArrMax = maxt

	### Debug Functions ###

	def printTimes(self):
		print(self.clockTimes)

	def getAllCustomers(self):
		return self.clockTimes

	def getCurrentCustomer(self, time):
		return self.clockTimes[time]

	def getLastCustomerTime(self):
		return self.clockTimes[-1]

