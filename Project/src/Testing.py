'''
Jacob McKenna
UAF CS 680 Advanced Discrete Event Simulation 
Employee Class
'''

import Employee 
import Account
t = Employee.Employee('10-1234567')

t.printDistribution()
t.service(3, 'test')
t.service(3, 'test')


a = Account.Account(100)

a.deposit(100.00)
print(a.getBalance())
a.withdraw(50.00)
print(a.getBalance())
a.withdraw(500.00)

