'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
ATM Class
'''

import random as rand

class ATM(object):


	def __init__(self):

		self.atmNum = rand.randint(1000, 3000)
		