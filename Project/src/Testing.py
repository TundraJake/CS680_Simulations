'''
Jacob McKenna
UAF CS 680 Advanced Discrete Event Simulation 
Employee Class
'''
import Employee 
import Product


l1,l2,l3 = Product.returnSetup()

for i in l1:
	print(i)

for i in l2:
	print(i)

for i in l3:
	print(i)

# p = Product.PRODUCTS
# prods = []

# for i, v in p.items():
# 	prods.append(Product.Product(i,v))


# p = Product.WRAPPERS
# prods = []

# for i,v  in p.items():
# 	print(i,v)



# print()
# for i, v in p.items():
# 	prods.append(Product.Wrapper(i,v))

# for i in prods:
# 	print(i.getName())


# w = Product.WRAPPERS

# for k,v in w.items():
# 	print(k, v)