'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Stockpile
'''

import random as rand

class Stockpile(object):

	def __init__(self, d1mat, location):
		self.__d1mat = d1mat
		self.__location = location # location is an int along a straight road

	def addD1Mat(self, truck):
		self.__d1mat += truck.dump(); 