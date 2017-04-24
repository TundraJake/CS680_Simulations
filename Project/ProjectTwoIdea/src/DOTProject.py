'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: DOTProject
'''

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

class DOTProject(object):

	def __init__(self, budget, patches, numDumpTrucks, numOilTrucks):
		
		self.__budget = budget
		self.__road = Road.Road(patches)

		self.__vehicles = []
		for _ in range(numDumpTrucks):
			self.__vehicles.append(Dumptruck.Dumptruck(10,20))

		for _ in range(numDumpTrucks):
			self.__vehicles = append(Oiltruck.Oiltruck(30,40))

		self.__chipper = Chipper.Chipper(30,40)
