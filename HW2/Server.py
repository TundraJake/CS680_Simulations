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
		self.busy = False
		self.minTime = mint
		self.maxTime = maxt
		self.currentServeTime = 0 		

	def startService(self):
		if (self.currentServeTime == 0 and self.busy == False):
			self.setBusy() # Serving
			self.currentServeTime = rand.randint(self.minTime, self.maxTime)
			print(self.currentServeTime)

		else:
			print("Dude is busy")

	def serveTheFool(self):
		if (self.currentServeTime != 0):
			self.currentServeTime -= 1
			print("Stille working!!!")

		elif (self.currentServeTime == 0 and self.busy == True): 
			self.setBusy() # Not busy anymore. 
			print("He finished")


	def setBusy(self):
		self.busy = not self.busy


	### Debug Function ### 
