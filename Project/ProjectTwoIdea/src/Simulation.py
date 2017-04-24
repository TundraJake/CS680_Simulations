'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Sumulation
'''

import time # Used for the clock (seconds).
import random as rand
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import Image

from collections import deque

# Road
import Road
import Patch

# Vehicles
import Dumptruck
import Oiltruck
import Chipper
import Ironwolf
import Grader


# Stockpile 
import Stockpile

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation(object):

	def __init__(self, budget, patches, numDumpTrucks, numOilTrucks):
		self.__simClock = 0

		self.__budget = budget
		self.__road = Road.Road(patches)

		self.__numDumpTrucks = []
		for _ in range(numDumpTrucks):
			self.__numDumpTrucks.append(Dumptruck.Dumptruck(10,20))

		self.__numOilTrucks = []
		for _ in range(numOilTrucks):
			self.__numOilTrucks = append(Oiltruck.Oiltruck(30,40))

		self.__chipper = Chipper.Chipper(30,40)
		self.__ironwolf = Ironwolf.Ironwolf(10,30)
		self.__grader = Grader.Grader(40,80)
		
	def startSim(self, name):

		# print(self.arrivalTimes) # Testing times, functions correctly. 
		myIter = 0 
		served = 0

		while 1:

			time.sleep(1)
			self.__simClock += 1








