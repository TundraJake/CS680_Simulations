'''
Jacob McKenna
UAF CS 680 Discrete Event SImulation 
Server Class 
'''
import Customers 
import random as rand

class Server():

	def __init__(self, mint, maxt):
		self.averageServeTime = 0
		self.customersServed = 0
		self.busy = False
		self.minTime = mint
		self.maxTime = maxt
		self.currentServeTime = 0 		

	def startService(self):
		if (self.currentServeTime == 0 and not self.busy):
			self.toggleBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			print(self.currentServeTime)

		else:
			print("Dude is busy")

	def serveTheCustomer(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			#print("Still working!!!")

		elif (self.currentServeTime == 0): 
			self.toggleBusy() # Not busy anymore. 
			#print("He finished!")


	def getBusyState(self):
		return self.busy

	def toggleBusy(self):
		self.busy = not self.busy

	def getAverageServeTime(self):
		return self.averageServeTime



	### Debug Function ### 
