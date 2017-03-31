'''
Jacob McKenna 

UAF CS680 Advanced Discrete Event Simulation

All products are created here. Classes for simulation are also here.
'''

PRODUCTS = {

	# 'name': [lbs, number of bags, lbs per bag, cost$$ per box ]
	'Beef': [40.0, 8, 5.0, 63.92],
	'Steak': [40.0, 32, 1.25, 121.54],
	'Chicken': [40.0, 32, 1.25, 101.23],
	'Nacho Cheese': [37.5, 10, 3.75, 82.41],
	'Cheese': [30.0, 6, 5.0, 47.52],
	'Three Cheese': [30.0, 6, 5.0, 68.40],
	'Lettuce': [30.0, 6, 5.0, 42.42],
	'Tomatos': [20.0, 4, 5.0, 35.78],

	# 'name': [lbs, number of bags, number of shells, costs]
	'Hard Shell Taco Shell': [15.0, 6, 40, 37.56],
	'Six Inch Tortillas': [30.0, 24, 24, 57.23],
	'Ten Inch Tortillas': [30.0, 20, 12, 62.32],
	'Twelve Inch Tortillas': [30.0, 12, 6, 56.91]


}

class Product(object):

	def __init__(self, name, value):
		self.__name = name
		self.__boxPounds = value[0]
		self.__numberOfBags = value[1]
		self.__lbsPerBag = value[2]
		self.__costPerBox = value[3]

	def getName(self):
		return self.__name

	def getTotallbs(self):
		return self.__boxPounds

	def getNumberOfBags(self):
		return self.__numberOfBags

	def getLbsPerBag(self):
		return self.__lbsPerBag

	def getCostPerBox(self):
		return self.__costPerBox

	def setProductPrice(self, newprice):
		self.__costPerBox = newprice



WRAPPERS = {
	
	# 'name': [number of wrappers, cost $$]
	'Soft Shell Wrappers': [2000, 40.0],
	'Hard Shell Wrappers': [2000, 40.0],
	'Burrito Wrappers': [2000, 40.0]

}

class Wrapper(object):

	def __init__(self, name, value):
		self.__name = name
		self.__totalWrappers = value[0]
		self.__costPerBox = value[1]

	def getName(self):
		return self.__name

	def getTotalWrappers(self):
		return self.__totalWrappers

	def getName(self):
		return self.__costPerBox

	def setWrapperPrice(self, newprice):
		self.__costPerBox = newprice


DISHES = {
	
	# 'name': [size, cost $$]
	'Ten Pound Pans': [10, 15.00],
	'Two and Half Pound Pans': [2.5, 15.00]

}

class Dishes(object):


	def __init__(self, name, value):
		self.__name = name
		self.__size = value[0]
		self.__costPerDish = value[1]

	def getName(self):
		return self.__name

	def getSize(self):
		return self.__size

	def getCostPerDish(self):
		return self.__costPerDish

	def setDishPrice(self, newprice):
		self.__costPerDish = newprice

'''
The only time I want this file to be called is when the simulation is ran.
I've set it up to load everything and return Lists of all items, prebuilt. 
'''
p = PRODUCTS
prods = []
for i, v in p.items():
	prods.append(Product(i,v))

w = WRAPPERS
wraps = []
for i, v in w.items():
	wraps.append(Wrapper(i,v))

d = DISHES
dishes = []
for i, v in d.items():
	dishes.append(Dishes(i,v))

def returnSetup():
	return prods, wraps, dishes

# Return it all.
returnSetup()














