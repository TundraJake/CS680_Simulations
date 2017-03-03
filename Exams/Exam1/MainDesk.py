'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
MainDesk Class - First contact for client, sends them off on to another queue.
'''

import random as rand

class MainDesk():

	def __init__(self, mint, maxt):
		self.averageServeTime = 0
		self.busy = False
		self.minTime = mint
		self.maxTime = maxt
		self.currentServeTime = 0
		self.serverTimes = []
		self.queue1 = 0
		self.queue2 = 0
		self.queue3	= 0 

	def startService(self):
		if (self.currentServeTime == 0 and not self.busy):
			self.toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			self.serverTimes.append(self.currentServeTime)
			# print("This is the current server time %d." %(self.currentServeTime))
		# else:
		# 	print("Service already started.")

	'''
		assignQueue - Assign Queue ranges from 0 to 100. This is a variable function, not a part of the exam.
	'''
	def assignQueue(self):
		self.queue1 = rand.randint(0, 100)
		self.queue2 = rand.randint(0, 100 - self.queue1)
		self.queue3 = 100 - self.queue1 - self.queue2
		print("q1,q2,q3 = [%d, %d, %d]" % (self.queue1, self.queue2, self.queue3))


		# Needs to be rewritten.... 
	def assignQueue1(self, newVal):
		self.queue1 = newVal
	def assignQueue2(self, newVal):
		self.queue2 = newVal
	def assignQueue3(self, newVal):
		self.queue3 = newVal

	'''
		assignQueue - Assign Queue ranges from 0 to 100. This is required for exam. 
	'''
	def examQueue(self):
		val = rand.randint(1,10)
		if val >= 1 and val <= 4:
			print("DL queue")
		elif val >= 5 and val <= 8:
			print("RG queue")
		elif val >= 9 and val <= 10:
			print("BO queue")

	def serveTheCustomer(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			# print("Server is busy.")

		elif (self.currentServeTime == 0 and self.busy): 
			# print("Finished Serving, not busy anymore.")
			self.toggleBusy() # Not busy anymore.

		# else:
			# print("Currently not busy.")


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
