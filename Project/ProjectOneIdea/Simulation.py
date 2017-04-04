'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Server Class 
'''
import time # Used for the clock (seconds).
import Server
import Customers
import random as rd
import matplotlib.pyplot as plt
import FEL

from collections import deque

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation():

    def __init__(self, numCust):

        self.simClock = 0
        self.FEL = FEL.FEL()
        # FEL list for now, no proper FEL is in place yet.
        # Represents customers. I'll use a class to represent this later.
        self.maxQueueLength = 0

    def startSim(self, name):

        waitTimes = []

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 

        print(self.arrivalTimes)
        while 1:

            self.serve1()
            self.serve2()
            self.incrementWaitTime()

            if self.arrivalTimes[myIter] == self.simClock:

                self.queue.append(self.arrivalTimes[myIter])
                self.queueLengths.append(len(self.queue))

                if self.maxQueueLength < len(self.queue):
                    self.maxQueueLength = len(self.queue)

                # print("Line length %d" % len(self.queue))

                myIter += 1
                if myIter == self.totalCustomers:
                    myIter = self.totalCustomers - 1

            # The first available server will be selected to serve the next customer.
            # Server One is the default Server. 
            if (not self.server1.getBusyState() and len(self.queue) > 0):
                self.queue.popleft()
                self.beginServing1()
                self.serve1()
                self.servedCustomers += 1
                # print("\nServer One Now serving next customer at time %d.\n" % (self.simClock))

            if (not self.server2.getBusyState() and len(self.queue) > 0):
                self.queue.popleft()
                self.beginServing2()
                self.serve2()
                self.servedCustomers += 1

                # print("\nServer Two Now serving next customer at time %d.\n" % (self.simClock))

            # else:

                # print("No customer to serve or both servers are busy.")
            holder = self.finalizeWaitTime()
            waitTimes.append(holder)
            print("The average wait time right now is %f at time %d." %(self.waitTime, self.simClock))
            self.simClock += 1

            ##############################################################################
            ''' Uncomment print functions and change speed to see results in real time!'''
            ##############################################################################
            time.sleep(.0001) # 1000 iterations/simulation seconds per second. Used to quickly speed up a simulation. 
            print("The total number of customer is = %d." %(self.totalCustomers))
            if (not self.server1.getBusyState() and not self.server2.getBusyState() and self.servedCustomers == self.totalCustomers):
                break


        # print("End of Simulation %s." % (name))
        # self.setAndPrintServerResults()
        # self.finalizeWaitTime()
        # print("The maximum queue length is %d." % (self.maxQueueLength))
        # print("Server One Serve Rate = [%d, %d]." %(self.s1m, self.s1M))
        # print("Server One Serve Rate = [%d, %d]." %(self.s2m, self.s2M))
        # print("Customer Arrival Rate = [%d, %d]." %(self.cAm, self.cAM))
        # print("Average Wait Time is %03f.\n" % (self.waitTime))

        plt.plot(waitTimes)
        plt.title("Figure " + str(name) + " for Queue Lengths")
        plt.xlabel("times(s)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(name) + "_for_ql.png")
        plt.clf()

        # plt.plot(self.server1ServerTimes)
        # plt.title("Figure " + str(name) + " for Server One")
        # plt.xlabel("# of Customers Served")
        # plt.ylabel("Serve Time")
        # plt.savefig("Sim_" + str(name) + "_for_s1.png")
        # plt.clf()

        # plt.plot(self.server2ServerTimes)
        # plt.title("Figure " + str(name) + " for Server Two")
        # plt.xlabel("# of Customer Served")
        # plt.ylabel("Serve Time")
        # plt.savefig("Sim_" + str(name) + "_for_s2.png")
        # plt.clf()



