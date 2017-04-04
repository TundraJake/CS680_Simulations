'''
Jacob McKenna 

UAF CS680 Advanced Discrete Event Simulation

All products are created here. Classes for simulation are also here.
'''

PRODUCTS = {

	# 'name': [id, lbs, number of bags, lbs per bag, cost$$ per box ]
	'Beans'			: [0, 40.0, 8, 5.0, 43.23],
	'Beef'			: [1, 40.0, 8, 5.0, 63.92],
	'Steak'			: [2, 40.0, 32, 1.25, 121.54],
	'Chicken'		: [3, 40.0, 32, 1.25, 101.23],
	'Nacho Cheese'	: [4, 37.5, 10, 3.75, 82.41],
	'Potatoes' 		: [5, 30.0, 6, 5.0, 39.99],

	#Cold Ingredients
	'Cheese'		: [6, 30.0, 6, 5.0, 47.52],
	'Three Cheese'	: [7, 30.0, 6, 5.0, 68.40],
	'Lettuce'		: [8, 30.0, 6, 5.0, 42.42],
	'Tomatoes'		: [9, 20.0, 4, 5.0, 35.78],

	# 'name': [id, lbs, number of bags, number of shells, costs]
	'Hard Shell Taco Shell'	: [10, 15.0, 6, 40, 37.56],
	'Six Inch Tortillas'	: [11, 30.0, 24, 24, 57.23],
	'Ten Inch Tortillas'	: [12, 30.0, 20, 12, 62.32],
	'Twelve Inch Tortillas'	: [13, 30.0, 12, 6, 56.91],

	# Misc. 
	'Potatoes' 				: [14, 30.0, 6, 5.0, 39.99],

	# 'name' : [id, lbs, number of tubes, clicks(serving) per tube, cost $$]
	'Sour Cream'			: [15, 36, 24, 20, 47.93],

	# 'name' : [id, lbs, number of bags, pounds per bag, cost $$]
	'Diced Onions' 			: [16, 10, 5, 2, 22.31]

}

class Product(object):

	def __init__(self, name, value):
		self.__name = name
		self.__id = value[0]
		self.__boxPounds = value[1]
		self.__numberOfBags = value[2]
		self.__lbsPerBag = value[3]
		self.__costPerBox = value[4]

	def getID(self):
		return self.__id

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
	
	# 'name': [id, number of wrappers, cost $$]
	'Soft Shell Wrappers'	: [0, 2000, 40.0],
	'Hard Shell Wrappers'	: [1, 2000, 40.0],
	'Burrito Wrappers'		: [2, 2000, 40.0]

}

class Wrapper(object):

	def __init__(self, name, value):
		self.__name = name
		self.__id = value[0]
		self.__totalWrappers = value[1]
		self.__costPerBox = value[2]

	def getID(self):
		return self.__id

	def getName(self):
		return self.__name

	def getTotalWrappers(self):
		return self.__totalWrappers

	def getName(self):
		return self.__costPerBox

	def setWrapperPrice(self, newprice):
		self.__costPerBox = newprice

DISHES = {
	
	# 'name': [id, size, cost $$]
	'Ten Pound Pans'			: [0, 10, 15.00],
	'Two and Half Pound Pans'	: [1, 2.5, 15.00]

}

class Dishes(object):

	def __init__(self, name, value):
		self.__name = name
		self.__id = value[0]
		self.__size = value[1]
		self.__costPerDish = value[2]

	def getID(self):
		return self.__id

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














