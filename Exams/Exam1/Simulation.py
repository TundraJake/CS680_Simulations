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

        self.custArrival = []

        self.custs = Customers.Customers(self.closes, ctm, ctM)
        totalCustomers = len(self.custs.getAllCustomers())
        for i in range(totalCustomers):

            time = self.custs.getCurrentCustomer(i)
            name = 'c' + str(i)

            self.custArrival.append(time)

            FELItem = [time, name, 'arr']
            self.FEL.pushEvent(FELItem)

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
            self.BOServers.append(Server.Server(self.bom, self.boM, "BO0", self.exam))

        else:
            print("not implemented yet!!!")

    

    def startSim(self, name):

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 
        served = 0

        print(self.custArrival)

        while 1:

            print("\nTime = %d" %(self.simClock))

            MDresult = self.mainDesk.serveTheCustomer(self.simClock)

            if not MDresult:
                print()

            elif MDresult[2] == 'DL Queue':
                print('dl queue')
                print(MDresult)
                self.DLServerQueue.append(MDresult)
                print("appending to DL, new size %d." % (len(self.DLServerQueue)))

            elif MDresult[2] == 'VR Queue':
                print('vr queue')
                print(MDresult)
                self.VRServerQueue.append(MDresult)
                print("appending to VR, new size %d." % (len(self.VRServerQueue)))

            elif MDresult[2] == 'BO Queue':
                print('bo queue')
                print(MDresult)
                self.BOServerQueue.append(MDresult)  
                print("appending to BO, new size %d." % (len(self.BOServerQueue)))

            # Service all queues
            for i in range(len(self.DLServers)):
                self.DLServers[i].serveTheCustomer()

            for i in range(len(self.VRServers)):
                self.VRServers[i].serveTheCustomer()

            for i in range(len(self.BOServers)):
                self.BOServers[i].serveTheCustomer()







            if self.custArrival[myIter] == self.simClock:

                self.MDServerQueue.append(self.FEL.popEvent())
                # self.queueLengths.append(len(self.MDServerQueue))

                if self.MDmaxQueueLengths < len(self.MDServerQueue):
                    self.MDmaxQueueLengths = len(self.MDServerQueue)

                myIter += 1
                if myIter == self.totalCustomers:
                    myIter -= 1 # avoids out of bound access


            if (not self.mainDesk.getBusyState() and len(self.MDServerQueue) > 0):
                customer = self.MDServerQueue.popleft()
                start, stop = self.mainDesk.service(self.simClock, customer)
                self.mainDesk.serveTheCustomer(self.simClock)
                # print(start)
                # print("what the frick")
                # print(stop)
                # print("why are you being crap")
                # self.FEL.pushEvent(start)
                # self.FEL.pushEvent(stop)

            for i in range(len(self.DLServers)):
                if (not self.DLServers[i].getBusyState() and len(self.DLServerQueue) > 0):
                    print('\n')
                    customer = self.DLServerQueue.popleft()
                    start, stop = self.DLServers[i].service(self.simClock, customer)
                    print(customer)
                    print(start)
                    print(stop)
                    self.DLServers[i].serveTheCustomer()
                    print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.DLServers[i].getServerID()))
                    served += 1

            for i in range(len(self.VRServers)):
                if (not self.VRServers[i].getBusyState() and len(self.VRServerQueue) > 0):
                    print('\n')
                    customer = self.VRServerQueue.popleft()
                    start, stop = self.VRServers[i].service(self.simClock, customer)
                    print(customer)
                    print("here's the bug for vr")
                    print(start)
                    print(stop)
                    self.VRServers[i].serveTheCustomer()
                    print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.VRServers[i].getServerID()))
                    served += 1

            for i in range(len(self.BOServers)):
                if (not self.BOServers[i].getBusyState() and len(self.BOServerQueue) > 0):
                    print('\n')
                    customer = self.BOServerQueue.popleft()
                    start, stop = self.BOServers[i].service(self.simClock, customer)
                    print(customer)
                    print("here's the bug for bo")
                    print(start)
                    print(stop)
                    self.BOServers[i].serveTheCustomer()
                    print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.BOServers[i].getServerID()))
                    served += 1

            print('\n')
            print("MD server queue = %d" %(len(self.MDServerQueue)))
            print("DL server queue = %d" %(len(self.DLServerQueue)))
            print("VR server queue = %d" %(len(self.VRServerQueue)))
            print("BO server queue = %d" %(len(self.BOServerQueue)))

            time.sleep(.008)
            print(self.totalCustomers)
            print(served)
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

