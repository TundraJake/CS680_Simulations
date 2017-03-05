'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
MainDesk Class - First contact for client, sends them off on to another queue.
'''

import random as rand
import Server

class MainDesk(Server.Server):

	def __init__(self, mint, maxt):
		super().__init__(mint, maxt)
		self.queue1Dist = 0 
		self.queue2Dist = 0 
		self.queue3Dist = 0 

	'''
		randomQueueDistribution - Sets a random distribution for DL, VR, and BO queues. 
	'''
	def randomQueueDistribution(self):
		self.queue1Dist = rand.randint(0, 100)
		self.queue2Dist = rand.randint(0, 100 - self.queue1Dist)
		self.queue3Dist = 100 - self.queue1Dist - self.queue2Dist
		print("q1,q2,q3 = [%d, %d, %d]" %(self.queue1Dist, self.queue2Dist, self.queue3Dist))

	'''
		randonQueueAssignment - Assign Queue ranges from 0 to 100. This is a variable function, not a part of the exam.
	'''
	def randomQueueAssignment(self):
		rval = rand.randint(1,100)
		q1q2 = (self.queue1Dist + self.queue2Dist)
		if rval >= 1 and rval <= self.queue1Dist:
			return "DL"
		elif rval >= self.queue1Dist and rval <= q1q2:
			return "VR"
		elif rval >= q1q2 and rval <= 100:
			return "BO"


	'''
		examQueueAssignment - Exam required distribution. 
	'''
	def examQueueAssignment(self):
		rval = rand.randint(1,10)
		if rval >= 1 and rval <= 4:
			return "DL"
		elif rval >= 5 and rval <= 8:
			return "VR"
		elif rval >= 9 and rval <= 10:
			return "BO"

