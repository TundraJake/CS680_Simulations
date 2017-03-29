'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Money Class
'''

import random as rand

class Money(object):

	def __init__(self):
		self.__pennies = rand.randint(0, 20)
		self.__dimes = rand.randint(0, 4)
		self.__nickels = rand.randint(0, 2)
		self.__quarters = rand.randint(0, 3)
		self.__ones = rand.randint(0, 10)
		self.__twos = rand.randint(0, 1)
		self.__fives = rand.randint(1, 4)
		self.__tens = rand.randint(0, 5)
		self.__twenties = rand.randint(0, 5)
		self.__fifties = rand.randint(0, 2)
		self.__hundreds = rand.randint(0, 1)


