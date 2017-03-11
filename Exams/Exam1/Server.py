'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Server Class 
'''
import Customers 
import random as rand
import numpy as np

class Server(object):

	def __init__(self, minTime, maxTime, serverID):
		self.busy = False
		self.minTime = minTime
		self.maxTime = maxTime
		self.serverID = serverID
		self.currentServeTime = 0
		self.serverTimes = []
		self.servingCustomer = [] # 3 element list

	def service(self, time, customer):
		if (self.currentServeTime == 0 and not self.busy):
			self.toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			self.servingCustomer = customer
			print("Servicing customer %s at %s" %(self.servingCustomer[1], self.serverID))
			return [time, self.serverID, 'start'], [time + self.currentServeTime, self.serverID, 'stop']

	__service = service
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	def serveTheCustomer(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			# print("Server is busy.")

		elif (self.currentServeTime == 0 and self.busy): 
			print("Finished Serving, not busy anymore for %s." %(self.serverID))
			self.toggleBusy() # Not busy anymore.

	__serveTheCustomer = serveTheCustomer

		# else:
			# print("Currently not busy.")

	def printCustomersServed(self):
		print(len(self.serverTimes))

	def getServerID(self):
		return self.serverID

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
		print("[Min, Max] = [%d, %d]." % (self.minTime, self.maxTime))
