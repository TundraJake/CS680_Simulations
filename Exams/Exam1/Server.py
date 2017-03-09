'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Server Class 
'''
import Customers 
import random as rand

class Server(object):

	def __init__(self, mint, maxt, serverID, exam):
		self.averageServeTime = 0
		self.busy = False
		self.minTime = mint
		self.maxTime = maxt
		self.serverID = serverID
		self.currentServeTime = 0
		self.serverTimes = []
		self.servingCustomer = [] # 3 element list
		self.exam = exam

	def service(self, time, customer):
		if (self.currentServeTime == 0 and not self.busy):
			self.toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			self.servingCustomer = customer
			print("Servicing customer %s." %(self.servingCustomer[1]))
			return [time, self.serverID, 'start'], [time + self.currentServeTime, self.serverID, 'stop']

	__service = service
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	def serveTheCustomer(self):
		print(self.currentServeTime)
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			# print("Server is busy.")

		elif (self.currentServeTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore.")
			self.toggleBusy() # Not busy anymore.

	__serveTheCustomer = serveTheCustomer

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

