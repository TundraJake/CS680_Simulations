'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Account Class
'''

import random as rand

class Account(object):

	def __init__(self, initialDeposit):

		self.__balance = initialDeposit

		# Four digit pin number
		self.__pin = ''
		for _ in range(4): 
			self.__pin = rand.choice('1234567890')


	def deposit(self, amount):

		self.__balance += amount

	def withdraw(self, amount):

		if (self.__balance - amount) < 0:

			print("Cannot withdraw more than you have")
			return 0

		else:

			self.__balance = self.__balance - amount
			print('New Balance = %.2f' %(self.__balance))
			return amount

	def getBalance(self):

		return self.__balance

