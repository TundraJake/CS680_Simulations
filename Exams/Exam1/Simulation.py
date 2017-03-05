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
import MainDesk

from collections import deque

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation():

    def __init__(self, mdm, mdM, dlm, dlM, vrm, vrM, bom, boM, examORrandom):

        self.simClock = 0
        # Main Desk
        self.mdm = mdm
        self.mdM = mdM
        # Driver License
        self.dlm = dlm
        self.dlM = dlM
        # Vehicle Registration
        self.vrm = vrm 
        self.vrM = vrM
        # Both 
        self.bom = bom
        self.boM = boM

        self.DLServers = []
        self.VRServers = []
        self.BOServers = []
        # FEL list for now, no proper FEL is in place yet.
        # Represents customers. I'll use a class to represent this later.
        self.arrivalTimes = [] 
        self.maxQueueLength = 0
        self.waitTime = 0
        self.queueLengths = []

        # self.mainDeak = MainDesk.MainDesk()
        if examORrandom: # If True, Exam, else random.
            for _ in range(2):
                self.DLServers.append(Server.Server(self.dlm, self.dlM))
                self.VRServers.append(Server.Server(self.vrm, self.vrM))
            self.BOServers.append(Server.Server(self.bom, self.boM))

        print(len(self.DLServers))
        print(len(self.VRServers))
        print(len(self.BOServers))
 
        

        self.servedCustomers = 0 # Both used to track when all customers have been served.
        
        self.mainDeskServeTimes = []

        self.averageQueueLength = 0
        self.queue = deque()
        self.averageQueueLengthPerSecond = [] # Holds a list of average queue length over time.     

        clock = 0


    ''' 
    I chose to average the time over the entire simulation, even though the end period may be longer
    than the last customer served. Until I can refactor this into a proper Future Event List, this will be the optimal
    solution until then. 
    '''
        
    def incrementWaitTime(self):
        self.waitTime += len(self.queue)

    def finalizeWaitTime(self):
        self.waitTime = (self.waitTime / self.totalCustomers)

    def startSim(self, name):

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 

        while 1:

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

            # # The first available server will be selected to serve the next customer.
            # # Server One is the default Server. 
            # if (not self.server1.getBusyState() and len(self.queue) > 0):
            #     self.queue.popleft()
            #     self.beginServing1()
            #     self.serve1()
            #     self.servedCustomers += 1
            #     # print("\nServer One Now serving next customer at time %d.\n" % (self.simClock))

            # if (not self.server2.getBusyState() and len(self.queue) > 0 and self.server1.getBusyState()):
            #     self.queue.popleft()
            #     self.beginServing2()
            #     self.serve2()
            #     self.servedCustomers += 1

            #     # print("\nServer Two Now serving next customer at time %d.\n" % (self.simClock))

            # else:

                # print("No customer to serve or both servers are busy.")
                
            self.simClock += 1

            ##############################################################################
            ''' Uncomment print functions and change speed to see results in real time!'''
            ##############################################################################
            time.sleep(.0001) # 1000 iterations/simulation seconds per second. Used to quickly speed up a simulation. 

            if (not self.server1.getBusyState() and not self.server2.getBusyState() and self.servedCustomers == self.totalCustomers):
                break


'''        
        print("End of Simulation %s." % (name))
        self.setAndPrintServerResults()
        self.finalizeWaitTime()
        print("The maximum queue length is %d." % (self.maxQueueLength))
        print("Server One Serve Rate = [%d, %d]." %(self.s1m, self.s1M))
        print("Server One Serve Rate = [%d, %d]." %(self.s2m, self.s2M))
        print("Customer Arrival Rate = [%d, %d]." %(self.cAm, self.cAM))
        print("Average Wait Time is %03f.\n" % (self.waitTime))

        plt.plot(self.queueLengths)
        plt.title("Figure " + str(name) + " for Queue Lengths")
        plt.xlabel("# of Customers Served")
        plt.ylabel("Queue Length")
        plt.savefig("Sim_" + str(name) + "_for_ql.png")
        plt.clf()

        plt.plot(self.server1ServerTimes)
        plt.title("Figure " + str(name) + " for Server One")
        plt.xlabel("# of Customers Served")
        plt.ylabel("Serve Time")
        plt.savefig("Sim_" + str(name) + "_for_s1.png")
        plt.clf()

        plt.plot(self.server2ServerTimes)
        plt.title("Figure " + str(name) + " for Server Two")
        plt.xlabel("# of Customer Served")
        plt.ylabel("Serve Time")
        plt.savefig("Sim_" + str(name) + "_for_s2.png")
        plt.clf()

'''

