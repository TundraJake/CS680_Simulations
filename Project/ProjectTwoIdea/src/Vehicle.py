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
		self.totalStateGraphList = []
		self.stateGraphList = []

		self.currentPatch = 0
		self.totalPatches = 0
		self.vehicleSpeed = 0 

		self.utilTime = 0

		self.patch = ''
		self.state = 0

		self.vehicleCostPerMinute = 0
		self.vehicleTotalCost = 0

		self.employeeCostPerMinute = 0
		self.employeeTotalCost = 0
		
		self.movesLeft = 0 

	def getName(self):
		return self.name

	def getState(self):
		return self.state

	def toggleBusy(self):
		self.busy = not self.busy

	def moveToNextPatch(self):
		self.currentPatch += 1

		if(self.currentPatch > 49):
			self.currentPatch = 49

	def generateDailyFuelAndHourlyCost(self):

		self.vehicleTotalCost += self.vehicleCostPerMinute

		self.employeeTotalCost += self.employeeCostPerMinute

	def getVehicleCosts(self):
		print(self.name, 'vehicle cost', self.vehicleTotalCost)
		return self.vehicleTotalCost

	def getEmployeeCosts(self):
		print(self.name, 'employee cost', self.employeeTotalCost)
		return self.employeeTotalCost

	def genUtilGraphs(self, simNumName, day):

		plt.plot(self.utilGraphList)
		plt.ylim([0,1])
		plt.xlim([0, 800])
		plt.title(self.name + ' Utilization Graph Day ' + str(day))
		# l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
		# l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
		# plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
		plt.xlabel("time(m)")
		plt.ylabel("Percent Busy")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/util/'  + str(self.name) + 'day' + str(day) + ".png", bbox_inches='tight')
		plt.cla()
		plt.close()

		self.utilTime = 0
		self.utilGraphList = []

	def genUtilTime(self, simClock):

		holder = (self.utilTime / simClock)
		self.utilGraphList.append(holder)

		self.generateDailyFuelAndHourlyCost()


	def genStateGraphs(self, simNumName, xpoints, day):

		plt.step(xpoints, self.stateGraphList)
		plt.xlim([0, 6])
		plt.xlim([0, 800])
		plt.title(self.name + ' Utilization Graph Day ' + str(day))
		# l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
		# l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
		# plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
		plt.xlabel("time(m)")
		plt.ylabel("State")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/state/'  + str(self.name) + 'day' + str(day) + ".png", bbox_inches='tight')
		plt.cla()
		plt.close()

		self.stateGraphList = []


	def changeState(self, newState):

		self.state = self.states[newState]	

	def appendState(self):
		self.totalStateGraphList.append(self.state)
		self.stateGraphList.append(self.state)
















