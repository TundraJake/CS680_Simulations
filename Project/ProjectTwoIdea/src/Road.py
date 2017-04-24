'''
Jacob McKenna
UAF CS680 Advanced Discrete Event Simulation 
Class: Road
'''
import time
import Pickup
import Ironwolf
import Grader
import Oiltruck
import Chipper
import RubberTireRoller
import Dumptruck

import Patch
import random as rand
class Road(object):
	
	def __init__(self, numPatches):

		### Number Of Patches ###
		self.patches = []
		self.totalArea = 0

		# May start right on the first mile. 
		start = rand.randint(0, 2000)

		for i in range(numPatches):

			length = rand.randint(100, 3600)

			### Total Square feet
			self.patches.append(Patch.Patch(start, length))
			self.totalArea += self.patches[i].getArea()

			start += length

			# start has to be at least 100 feet from the previous patch. 
			start += rand.randint(100, 2000) 

	def getTotalPatchArea(self):
		return str(self.totalArea) + " Sqaure Feet"

	def getPatch(self, currentPatch):
		return self.patches[currentPatch]

road = Road(100)
pickup = Pickup.Pickup(3,6)
iron = Ironwolf.Ironwolf(15,20)
grader = Grader.Grader(10,11)
oil = Oiltruck.Oiltruck(5,10)
chipper = Chipper.Chipper(10,15)
rtr = RubberTireRoller.RubberTireRoller(15,30)

x = 0 
while x < 10000000:

	if (not pickup.busy):
		pickup.startWork(road)

	if (not iron.busy):
		iron.startWork(road)
	
	if (not grader.busy):
		grader.startWork(road)

	if (not oil.busy):
		oil.startWork(road)

	if (not chipper.busy):
		chipper.startWork(road)

	if (not rtr.busy):
		rtr.startWork(road)

	pickup.work()
	grader.work()
	iron.work()
	oil.work()
	chipper.work()
	rtr.work()



	# time.sleep(.25)
	print(road.patches[0].getState(), "patch 1")
	print(road.patches[1].getState(),"patch 2")
	print(road.patches[2].getState(),"patch 3")
	print(road.patches[3].getState(),"patch 4")
	print(road.patches[4].getState(),"patch 5")
	x += 1





