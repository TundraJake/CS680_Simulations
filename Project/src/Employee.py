'''
Jacob McKenna
UAF CS 680 Advanced Discrete Event Simulation 
Employee Class
'''
#
import Customer 
import random as rand
import numpy as np
import names

class Employee(object):

	def __init__(self, ID):
		self.__busy = False
		self.__firstName = names.get_first_name()
		self.__lastName = names.get_last_name()
		self.__minTime = rand.randint(1,5)
		self.__maxTime = self.__minTime + rand.randint(1,5)
		self.__ID = ID
		self.__currentServeTime = 0
		self.__serverTimes = []
		self.__servingCustomer = [] # 3 element list
		self.__utilTime = []

	def service(self, time, customer):
		if (self.__currentServeTime == 0 and not self.__busy):
			self.toggleBusy() # Serving
			self.__currentServeTime = rand.randint(self.__minTime, self.__maxTime)
			self.__serverTimes.append(self.__currentServeTime)
			self.__servingCustomer = customer
			# print("Servicing customer %s at %s" %(self.servingCustomer[1], self.ID))
			# return [time, self.ID, 'start'], [time + self.currentServeTime, self.ID, 'stop']

	__service = service
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	def serveTheCustomer(self):
		if (self.__currentServeTime != 0):
			self.__currentServeTime -= 1
			return 1
			# print("Server is busy.")

		elif (self.__currentServeTime == 0 and self.__busy): 
			# print("Finished Serving, not busy anymore for %s." %(self.ID))
			self.toggleBusy() # Not busy anymore.
			return 0

		else:
			return 0

	__serveTheCustomer = serveTheCustomer

		# else:
			# print("Currently not busy.")

	def getFirstName(self):
		return self.__firstName

	def getLastName(self):
		return self.__lastName

	def getFullName(self):
		return self.__firstName + " " + self.__lastName

	def appendUtilTimes(self, value):
		self.__utilTime.append(value)

	def getUtilTimes(self):
		return self.__utilTime

	def printCustomersServed(self):
		print("Server %s serviced %d custommers."%(self.__ID, len(self.__serverTimes)))

	def getServerID(self):
		return self.__ID

	def printServerTimes(self): ### Debug Function ###
		print(self.__serverTimes)

	def getServerTimes(self):
		return self.__serverTimes

	def getBusyState(self):
		return self.__busy

	def toggleBusy(self):
		self.__busy = not self.__busy

	def printAverageServeTime(self):
		print(np.mean(self.__serverTimes))

	def printDistribution(self):
		print("%s distribution for [Min, Max] = [%d, %d]." % (self.__ID, self.__minTime, self.__maxTime))
