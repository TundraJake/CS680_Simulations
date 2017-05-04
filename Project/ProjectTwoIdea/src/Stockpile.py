'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Stockpile - Both Oil and D1
'''

import random as rand
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from collections import deque

class Stockpile(object):

	def __init__(self, d1mat, oil,location):

		self.d1mat = d1mat
		self.oilTanker = oil

		self.location = location # location is an int along a straight road
		self.queue = deque()
		self.d1List = []
		self.oilList = []

		self.oilDeliveryCost = 0
		self.d1DeliveryCost = 0


	def addD1Mat(self):
		self.oilDeliveryCost += 34000 # $17,000
		self.d1mat += 1000 # 1000 cubic yards

	def addOil(self):
		self.d1DeliveryCost += 20000 # $20,000
		self.oilTanker += 7000 # 7,000 gallons 


	def getOilDeliveryCost(self):
		# print(self.oilDeliveryCost, ' Oil Delivery Cost')
		return self.oilDeliveryCost

	def getD1DeliveryCost(self):
		# print(self.d1DeliveryCost, ' D1 Delivery Cost')
		return self.d1DeliveryCost


	def loadDumpTruck(self):
		d1Amount = .5
		self.d1mat -= d1Amount

		if (self.d1mat <= 0):
			# print('d1 is empty')
			return 0
		else:
			return d1Amount




	def loadDistributor(self):
		oilAmount = 125
		self.oilTanker -= oilAmount

		if (self.oilTanker <= 0):
			# print('oil is empty')
			return 0
		else:
			return oilAmount



	def startLoadingOil(self, truck):
		self.queue.append(truck)

	def startLoading(self, truck):
		self.queue.append(truck)


	def appendResourceNodes(self):

		self.d1List.append(self.d1mat)
		self.oilList.append(self.oilTanker)


	def genD1matGraph(self,simNumName, day):

		plt.plot(self.d1List)
		# plt.ylim([0,1])
		# plt.xlim([0,100])
		plt.title('D1 Material Pit Day ' + str(day))
		plt.xlabel("time(m)")
		plt.ylabel("D1 Remaing (cubic yards)")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/resources/'  + 'd1mat' + 'day' + str(day) +  ".png", bbox_inches='tight')
		plt.clf()
		plt.close()

		self.oilList = []

	def getOilmatGraph(self,simNumName, day):

		plt.plot(self.oilList)
		# plt.ylim([0,1])
		plt.xlim([0, 720])
		plt.title('Oil Tanker Day ' + str(day))
		plt.xlabel("time(m)")
		plt.ylabel("Oil Remaining (gallons)")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/resources/'  + 'oilmat' + ".png", bbox_inches='tight')
		plt.clf()
		plt.close()
		self.d1List = []












