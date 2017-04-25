'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Vehicle
'''

import random as rand
import matplotlib.pyplot as plt

class Vehicle(object):

	def __init__(self, employeeMinTime, employeeMaxTime, name):
		self.busy = False
		self.name = name

		self.fuelTank = 0
		self.currentFuel = 0
		self.currentWorkTime = 0

		self.minTime = employeeMinTime
		self.maxTime = employeeMaxTime

		self.patchWorkTimes = []
		self.utilGraphItem = []

		self.currentPatch = 0
		self.totalPatches = 0
		self.vehicleSpeed = 0 

		self.utilTime = 0

		self.patch = ''
		self.state = 0

	def getState(self):
		return self.state

	def toggleBusy(self):
		self.busy = not self.busy

	def moveToNextPatch(self):
		if (self.totalPatches != self.currentPatch):
			self.currentPatch += 1	

	def genUtilGraphs(self, simNumName):
		
		plt.plot(self.utilGraphItem)
		plt.title(self.name + ' Utilization Graph')
		# l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
		# l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
		# plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
		plt.xlabel("time(m)")
		plt.ylabel("Percent Busy")
		plt.savefig('../graphs/' + str(simNumName) + "_for_" + str(self.name) + ".png", bbox_inches='tight')
		plt.clf()

	def generateWaitAndUtilizationTime(self, simClock):

		### Wait Times ###
		holder = (self.utilTime / simClock)
		self.utilGraphItem.append(holder)



















