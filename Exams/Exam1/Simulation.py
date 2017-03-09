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
        self.exam = exam

        self.custs = Customers.Customers(self.closes, ctm, ctM)
        totalCustomers = len(self.custs.getAllCustomers())
        for i in range(totalCustomers):
            item = [self.custs.getCurrentCustomer(i), 'c' + str(i), 'arr']
            self.FEL.pushEvent(item)

        self.totalCustomers = len(self.custs.getAllCustomers())

        # All Servers
    
        self.mainDesk = MainDesk.MainDesk(self.mdm, self.mdM, 'MD', self.exam)
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
        if self.exam: # If True, Exam, else random.
            for i in range(2):
                self.DLServers.append(Server.Server(self.dlm, self.dlM, 'DL' + str(i), self.exam))
                self.VRServers.append(Server.Server(self.vrm, self.vrM, 'VR' + str(i), self.exam))
            self.BOServers.append(Server.Server(self.bom, self.boM, "BO1", self.exam))

        else:
            print("not implemented yet!!!")

    

    def startSim(self, name):

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 
        served = 0
        custArrival = self.FEL.getFEL()

        while 1:

            self.mainDesk.serveTheCustomer(self.simClock)

            print('\n')
            self.FEL.printFEL()
            print('\n')

            # clock = self.custs.getCurrentCustomer(0)
            
            if custArrival[myIter][0] == self.simClock:

                self.MDServerQueue.append(custArrival[myIter])
                # self.queueLengths.append(len(self.MDServerQueue))

                if self.MDmaxQueueLengths < len(self.MDServerQueue):
                    self.MDmaxQueueLengths = len(self.MDServerQueue)

                # print("Line length %d" % len(self.queue))

                myIter += 1
                if myIter == self.totalCustomers:
                    myIter = self.totalCustomers - 1
        

            if (not self.mainDesk.getBusyState() and len(self.MDServerQueue) > 0):
                self.MDServerQueue.popleft()
                start, stop = self.mainDesk.service(self.simClock, custArrival[served])
                self.mainDesk.serveTheCustomer(self.simClock)
                self.FEL.pushEvent(start)
                self.FEL.pushEvent(stop)

                served += 1

            for i in range(len(self.DLServers)):
                if (not self.DLServers[i].getBusyState and len(self.DLServerQueue) > 0):
                    customer = self.DLServerQueue.popleft()
                    start, stop = self.DLServers[i].service(self.simClock, customer)
                    self.DLServers[i].serveTheCustomer()
                    # self.servedCustomers += 1
                print("something")

            for i in range(len(self.VRServers)):
                print("something again")


            for i in range(len(self.BOServers)):
                print("something twice again")


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
            self.simClock += 1 
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

