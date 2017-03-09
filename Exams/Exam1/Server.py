'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Server Class 
'''
import Customers 
import random as rand

class Server(object):

	def __init__(self, mint, maxt, serverID):
		self.averageServeTime = 0
		self.busy = False
		self.minTime = mint
		self.maxTime = maxt
		self.serverID = serverID
		self.currentServeTime = 0
		self.serverTimes = []		

	def startService(self):
		if (self.currentServeTime == 0 and not self.busy):
			toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	def serveTheCustomer(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			# print("Server is busy.")

		elif (self.currentServeTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore.")
			toggleBusy() # Not busy anymore.

		# else:
			# print("Currently not busy.")

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

	def getAverageServeTime(self):
		return self.averageServeTime

