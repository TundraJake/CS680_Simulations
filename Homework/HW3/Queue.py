'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Queue Class 
'''

from collections import deque 

class Queue(object):

	def __init__(self):
		self.queue = deque()
