class person(object):

	def __init__(self, name):
		self.__name = name

	def printName(self):
		print(self.__name)

	__print = printName

class employee(person):

	def __init__(self, name):
		super().__init__(name)

	def printName(self):
		print("This is an employee named %s." %(self._person__name))

e = employee("billy")
e.printName()