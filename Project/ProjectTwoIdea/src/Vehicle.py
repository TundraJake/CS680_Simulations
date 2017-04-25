'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Vehicle
'''

import random as rand
import math
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
		self.utilGraphList = []
		self.stateGraphList = []

		self.currentPatch = 0
		self.totalPatches = 0
		self.vehicleSpeed = 0 

		self.utilTime = 0

		self.patch = ''
		self.state = 0

		self.utilDir = ''
		self.stateDir = ''

	def getState(self):
		return self.state

	def toggleBusy(self):
		self.busy = not self.busy

	def moveToNextPatch(self):
		if (self.totalPatches != self.currentPatch):
			self.currentPatch += 1	



	def genUtilGraphs(self, simNumName):
		
		plt.plot(self.utilGraphList)
		plt.ylim([0,1])
		plt.title(self.name + ' Utilization Graph')
		# l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
		# l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
		# plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
		plt.xlabel("time(m)")
		plt.ylabel("Percent Busy")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/util/'  + str(self.name) + ".png", bbox_inches='tight')
		plt.clf()

	def genUtilTime(self, simClock):

		holder = (self.utilTime / simClock)
		self.utilGraphList.append(holder)



	def genStateGraphs(self, simNumName, xpoints):
		
		plt.step(xpoints, self.stateGraphList)
		plt.xlim([0, math.ceil( len (self.stateGraphList / 1000) * 1000 )])
		plt.title(self.name + ' Utilization Graph')
		# l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
		# l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
		# plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
		plt.xlabel("time(m)")
		plt.ylabel("State")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/state/'  + str(self.name) + ".png", bbox_inches='tight')
		plt.clf()



	def changeState(self, newState):

		self.state = self.states[newState]	



	def appendState(self):

		self.stateGraphList.append(self.state)
















