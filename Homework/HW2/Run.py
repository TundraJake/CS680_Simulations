'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Run File - Inits a simulation event of two servers and n customers.  
Many print functions may be uncommented to show bahavior of the simulation.
'''

import Server
import Simulation

# Simulation init func - 
# def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):

sim1 = Simulation.Simulation(3,4, 3,5, 100, 1,4)
sim1.startSim("1")
'''
sim1 Results - Customers are arriving relatively fast. Server Two services customers very quickly to the point significant
downtime occured for Server Two. Server One was almsot always twice as busy as Server Two.
	Test results yielded (all results are random!):
	Maximum queue length = 2, 3, 2, 3, 3 on multiple tests.
	Server One Busy Percentage ~ 89% +/- 2%
	Server One Average Serve Time ~ 7.5s +/- .2s
	Server Two Busy Percentage ~ 40% +/- 2%
	Server Two Average Serve Time ~ 1.5s +/- .2s

Server Two is very productive at servicing in this simulation, which means Server Two can be utilized elsewhere or Sever One
can be moved elsewhere. Steady state is achieved as it appraoches hovers around 2 to 3 customers in the queue at any time. 
'''

# sim2 = Simulation.Simulation(7,8, 6,8, 10000, 1,3)
# sim2.startSim("2")
'''
sim2 Results - With just a hundred customers, the queue (line) rapidly builds up as the servers cannot service
each customer quickly. Customers are arriving too fast. 
	Test results yielded (all results are random!):
	Maximum queue length = 42, 41, 42, 44, 43 on multiple tests.
	Server One Busy Percentage ~ 98% +/- 1%
	Server One Average Serve Time ~ 7.5s +/- .2s
	Server Two Busy Percentage ~ 98% +/- 1%
	Server Two Average Serve Time ~ 4. +/- .4

Servers were constantly busy due to both having high service times while customers were rapidly arriving. 
'''

# sim3 = Simulation.Simulation(7,8, 1,2, 100, 1,5)
# sim3.startSim("3")
'''
sim3 Results - There is even more downtime for each server. Server One compared to simulation 2, dropped a few percent
whele Server Two droped at least double on the runs. Queue times were relatively short due to the fact servicing and 
the mild customer arrival rate. 
	Test results yielded (all results are random!): 
	Maximum queue length = 2, 2, 3, 2, 3 on multiple tests.
	Server One Busy Percentage ~ 85% +/- 2%
	Server One Average Serve Time ~ 7.5s +/- .2s
	Server Two Busy Percentage ~ 31% +/- 2%
	Server Two Average Serve Time ~ 1.5 +/- .2
'''


# sim4 = Simulation.Simulation(2,5, 4,10, 100, 5,8)
# sim4.startSim("4")
'''
sim3 Results - I wanted to show that if customers arrive at such a slow pace that one server can handle them
quickly, then there is no need for a second server. I broke my code due to division by zero, so it was a
good test test!
	Test results yielded (all results are random!): 
	Maximum queue length =  on multiple tests.
	Server One Busy Percentage ~ 54% +/- 2%
	Server One Average Serve Time ~ 3.5s +/- .2s
	Server Two Busy Percentage ~ 0% +/- 0%
	Server Two Average Serve Time ~ 0s +/- 0s
'''


# sim5 = Simulation.Simulation(3,5, 3,5, 100, 1,2)
# sim5.startSim("5")
# '''
# Simple, Fun Test.
# '''


# sim6 = Simulation.Simulation(3,5, 3,5, 100, 1,4)
# sim6.startSim("6")
# '''
# Simple, Fun Test.
# '''

# sim7 = Simulation.Simulation(6,7, 8,11, 100, 3,5)
# sim7.startSim("7")
'''
I think this is the best test for steady state. Every other tests shows 1 as the steady state, which is fine. 
'''







