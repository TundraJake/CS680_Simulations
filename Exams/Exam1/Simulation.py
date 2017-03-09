'''
Jacob McKenna
UAF CS 680 Discrete Event Simulation 
Server Class 
'''
import time # Used for the clock (seconds).
import Server
import Customers
import random as rand
import matplotlib.pyplot as plt
import MainDesk
import FEL

from collections import deque

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation():

    def __init__(self, ctm, ctM, mdm, mdM, dlm, dlM, vrm, vrM, bom, boM, exam, opens, closes):

        self.simClock = 0
        self.FEL = FEL.FEL()
        # Customer Arrival Times
        self.ctm = ctm
        self.ctM = ctM 
        # Main Desk
        self.mdm = mdm
        self.mdM = mdM
        # Driver License
        self.dlm = dlm
        self.dlM = dlM
        # Vehicle Registration8
        self.vrm = vrm 
        self.vrM = vrM
        # Both 
        self.bom = bom
        self.boM = boM

        # Open and close times. Close time represents when last customer can be served.
        self.open = opens
        self.closes = closes

        newCusts = Customers.Customers(self.closes, ctm, ctM)
        totalCustomers = range(len(newCusts.getAllCustomers()))
        for i in totalCustomers:
            self.FEL.pushEvent(newCusts.getCurrentCustomer(i), 'c' + str(i), 'arr')

        # All Servers
        self.mainDesk = Server.Server(self.mdm, self.mdM, 'MD1')
        self.MDServerQueue = deque()
        self.MDwaitTime = 0
        self.MDmaxQueueLengths = 0

        self.DLServers = []
        self.DLServerQueue = deque()
        self.DLwaitTime = 0
        self.DLmaxQueueLengths = 0

        self.VRServers = []
        self.VRServerQueue = deque()
        self.VRwaitTime = 0
        self.VRmaxQueueLengths = 0

        self.BOServers = []
        self.BOServerQueue = deque()
        self.BOwaitTime = 0
        self.BOmaxQueueLengths = 0     

        # self.mainDesk = MainDesk.MainDesk()
        if exam: # If True, Exam, else random.
            for i in range(2):
                self.DLServers.append(Server.Server(self.dlm, self.dlM, 'DL' + str(i)))
                self.VRServers.append(Server.Server(self.vrm, self.vrM, 'VR' + str(i)))
            self.BOServers.append(Server.Server(self.bom, self.boM, "BO1"))

        else:
            print("not implemented yet!!!")

    

    def startSim(self, name):

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 

        while 1:
            # self.incrementWaitTime()
        
            #     self.queue.append(self.arrivalTimes[myIter])
            #     self.queueLengths.append(len(self.queue))

            #     if self.maxQueueLength < len(self.queue):
            #         self.maxQueueLength = len(self.queue)

            #     # print("Line length %d" % len(self.queue))

            #     myIter += 1
            #     if myIter == self.totalCustomers:
            #         myIter = self.totalCustomers - 1

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
            time.sleep(.5) 
            # if (not self.server1.getBusyState() and not self.server2.getBusyState() and self.servedCustomers == self.totalCustomers):
            #     break


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

