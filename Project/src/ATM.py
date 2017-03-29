'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
ATM Class
'''

import random as rand

class ATM(object):


	def __init__(self):

		self.atmNumber = rand.randint(1000, 3000)
		self.