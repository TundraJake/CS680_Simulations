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



	def addD1Mat(self, truck):
		self.d1mat += truck.unload()

	def addOil(self, tanker):
		self.oilTanker += tanker.unload()



	def loadDumpTruck(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()

	def loadDistributor(self, truck):
		self.currentWorkTime = rand.randint(10, 20)
		truck.load()



	def startLoadingOil(self, truck):
		self.queue.append(truck)

	def startLoading(self, truck):
		self.queue.append(truck)



	def genD1matGraph(self):

		plt.plot(self.utilGraphList)
		plt.ylim([0,1])
		plt.xlim([0,100])
		plt.title('D1 Material Pit')
		plt.xlabel("time(m)")
		plt.ylabel("D1 Remaing (cubic yards)")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/resources/'  + 'd1mat' + ".png", bbox_inches='tight')
		plt.clf()

	def getOilmatGraph(self):

		plt.plot(self.utilGraphList)
		plt.ylim([0,1])
		plt.xlim([0,100])
		plt.title(self.name + ' Utilization Graph')
		plt.xlabel("time(m)")
		plt.ylabel("Oil Remaining (gallons)")
		plt.savefig('../sims/' + str(simNumName) + '/graphs/resources/'  + 'oilmat' + ".png", bbox_inches='tight')
		plt.clf()












