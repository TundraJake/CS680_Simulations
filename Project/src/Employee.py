'''
Jacob McKenna
UAF CS 680 Advanced Discrete Event Simulation 
Employee Class
'''
import Customer 
import random as rand
import numpy as np
import names

class Employee(object):

	def __init__(self):
		self.busy = False
		self.firstName = names.get_first_name()
		self.lastName = names.get_last_name()
		self.minTime = rand.randint(1,5)
		self.maxTime = self.minTime + rand.randint(1,5)
		self.ID = 0
		self.currentServeTime = 0
		self.serverTimes = []
		self.servingCustomer = [] # 3 element list
		self.utilTime = []

	def service(self, time, customer):
		if (self.currentServeTime == 0 and not self.busy):
			self.toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			self.servingCustomer = customer
			# print("Servicing customer %s at %s" %(self.servingCustomer[1], self.serverID))
			return [time, self.ID, 'start'], [time + self.currentServeTime, self.ID, 'stop']

	__service = service
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	def serveTheCustomer(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			return 1
			# print("Server is busy.")

		elif (self.currentServeTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			return 0

		else:
			return 0

	__serveTheCustomer = serveTheCustomer

		# else:
			# print("Currently not busy.")

	def appendUtilTimes(self, value):
		self.utilTime.append(value)

	def getUtilTimes(self):
		return self.utilTime

	def printCustomersServed(self):
		print("Server %s serviced %d custommers."%(self.ID, len(self.serverTimes)))

	def getServerID(self):
		return self.ID

	def printServerTimes(self): ### Debug Function ###
		print(self.serverTimes)

	def getServerTimes(self):
		return self.serverTimes

	def getBusyState(self):
		return self.busy

	def toggleBusy(self):
		self.busy = not self.busy

	def printAverageServeTime(self):
		print(np.mean(self.serverTimes))

	def printDistribution(self):
		print("%s distribution for [Min, Max] = [%d, %d]." % (self.ID, self.minTime, self.maxTime))
