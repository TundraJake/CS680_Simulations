
class person(object):
	def __init__(self, name):
		self.__name = name

	def printName(self):
		print(self.__name)

class employee(person):

	def __init__(self, name):
		super().__init__(name)


x = employee("timmy")
p = person("the hell are you")

x.printName()
p.printName()