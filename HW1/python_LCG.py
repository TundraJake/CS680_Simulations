# Jacob McKenna
# CS680 Advanced Discrete Event Simulations
# Assignment 1
# This assignment requires the implementation of the Linear 
# Congruential Method and five different test variable sets.
# The Kolmogorov Smirnov, mean, variance, and auto correlation tests. 
# These will also be applied to at least three different PRNGs. 

"""I have X| .5019, u| = .5, what test do we use to prove that this is a functioning 
PRNG 


S = .08399, SD = .083| 

* Is the difference too great that we need to reject it?
* X| - u| 

BUG in Graph Three

 
Go back and check the ACR graphs. 



Object oriented approach. That's how it is man.









"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as autoplt
import numpy as np
import random
from scipy import stats

# Linear Congruential Method Function
def lcg(seed, a,c,m):
    rand = (a*seed + c) % m
    return rand

    
def autocorr(series, histNum):

	series = np.asarray(series)
	n = len(series)
	data = np.asarray(series)
	mean = np.mean(data)
	c0 = np.sum((data - mean) ** 2) / float(n)

	def r(h):
		acf_lag = ((data[:n - h] - mean) * (data[h:] - mean)).sum() / float(n) / c0
		return round(acf_lag, 3)
	x = np.arange(n) # Avoiding lag 0 calculation
	acf_coeffs = list(map(r, x))

	plt.plot(acf_coeffs)
	if histNum == 1: 
		plt.ylim([-1,1])
	else:
		autoplt.ylim([-1,1])
	plt.title("LCG Spread Autocorrelation for LCG " + str(histNum))
	plt.xlabel("Value")
	plt.savefig("Autocorrelation" + str(histNum) + ".png")
	plt.show()


def statAndPlot(histList, histNum, X_0, a, c, m):

	mean = "The Mean = " + str('%.4f' % np.mean(histList))
	variance = "The Variance = " + str('%.5f' % np.var(histList))

	# Cycle Check
	first = histList[0]
	cycle = "m"
	count = 0
	for i in histList[1:]:
	    count = count + 1
	    if i == first:
	        cycle = count
	        break

	histList.sort()
	# Kolmogorov Smirnov Test
	result = stats.kstest(histList, 'norm')

	# r = np.correlate(histList, histList, mode = 'full')[-n:]
	# results = r/(variance*(np.arange(histList, 0, -1)))

	plt.hist(histList)
	plt.title("LCG Spread\n $X_0$ = " + str(X_0) +", a = " + str(a) + 
		", c = " + str(c) +", m = " + str(m) + ", Cycle = " + str(cycle) + "\n")
	plt.xlabel("Value\n\n" + mean + "\n" + variance + 
		"\n" + str(result) + "\n\nFigure " + str(histNum))
	plt.ylabel("Frequency")
	plt.savefig('hist' + str(histNum) + '.png', bbox_inches='tight')
	plt.show()


# Lists for test data. 
lcg_nums1 = []
lcg_nums2 = []
lcg_nums3 = []
lcg_nums4 = []
lcg_nums5 = []

# LCG 1.
seed = X_0 = 1
a = 1140671485
c = 128201163
m = 2**24 

for i in range(10000):
	seed = lcg(seed, a, c, m)
	lcg_nums1.append(seed/m)

autocorr(lcg_nums1, 1)
statAndPlot(lcg_nums1, 1, X_0, a, c, m)

# LCG 2. 
seed = X_0 = 7
a = 7
c = 7
m = 10.  

for i in range(10000):
	seed = lcg(seed, a, c, m)
	lcg_nums2.append(seed/m)

autocorr(lcg_nums2, 2)
statAndPlot(lcg_nums2, 2, X_0, a, c, m)

# LCG 3. # CHECK THIS GRAPH 
seed = X_0 = 1
a = 329
c = 100
m = 71

for i in range(10000):
	seed = lcg(seed, a, c, m)
	lcg_nums3.append(seed/m)

autocorr(lcg_nums3, 3)
statAndPlot(lcg_nums3, 3, X_0, a, c, m)

# LCG 4. 
seed = X_0 = 8
a = 1024
c = 2048
m = 51 

for i in range(10000):
	seed = lcg(seed, a, c, m)
	lcg_nums4.append(seed/m)

autocorr(lcg_nums4, 4)
statAndPlot(lcg_nums4, 4, X_0, a, c, m)

# LCG 5. 
seed = X_0 = 27
a = 17
c = 43
m = 100 

for i in range(10000):
	seed = lcg(seed, a, c, m)
	lcg_nums5.append(seed/m)

autocorr(lcg_nums5, 5)
statAndPlot(lcg_nums5, 5, X_0, a, c, m)


####################################################################
###################### Numbers from C++ Tests ######################
####################################################################

cPRNGs = np.loadtxt("prngNums.txt")


mean = "The Mean = " + str('%.4f' % np.mean(cPRNGs))
variance = "The Variance = " + str('%.5f' % np.var(cPRNGs))

# Cycle Check
first = cPRNGs[0]
cycle = "m"
count = 0
for i in cPRNGs[1:]:
    count = count + 1
    if i == first:
        cycle = count
        break

cPRNGs.sort()
# Kolmogorov Smirnov Test
result = stats.kstest(cPRNGs, 'norm')

plt.hist(cPRNGs)
plt.title("C++ STD LCG Test")
plt.xlabel("Value\n\n" + mean + "\n" + variance + 
		"\n" + str(result) + "\n\nFigure 1: C++ Test")
plt.ylabel("Frequency")
plt.savefig('histc++1.png', bbox_inches='tight')
plt.show()



