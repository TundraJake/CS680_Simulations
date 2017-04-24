'''
Jacob McKenna
UAF CS680 AdVanced Discrete Event Simulation 
Server Class 
'''
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
		self.utilTime = []

	def service(self):
		if (self.currentServeTime == 0 and not self.busy):
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			self.toggleBusy() # Serving
			self.serveTheCustomer()

			# print("Servicing customer %s at %s" %(self.servingCustomer[1], self.serverID))

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
			# print("Finished Serving, not busy anymore for %s." %(self.serverID))
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
		print("Server %s serviced %d custommers."%(self.serverID, len(self.serverTimes)))

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
		print("%s distribution for [Min, Max] = [%d, %d]." % (self.serverID, self.minTime, self.maxTime))
