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
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import Image

from collections import deque

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation():

    def __init__(self, ctm, ctM, mdm, mdM, dlm, dlM, vrm, vrM, bom, boM, opens, closes, numMD, numDL, numVR, numBO):

        self.simClock = 1
        self.FEL = FEL.FEL()
        self.timePoints = []
        # Customer Arrival Times
        self.ctm = ctm
        self.ctM = ctM 
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
        # Number of each server type
        self.numMD = numMD
        self.numDL = numDL
        self.numVR = numVR
        self.numBO = numBO

        # Open and close times. Close time represents when last customer can be served.
        self.opens = opens
        self.closes = closes

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
    
        self.MDServers = []
        self.MDServerQueue = deque()
        self.MDServerQueueLengths = []
        self.MDwaitTime = 0
        # Used for graph tracking/generation
        self.MDmaxQueueLength = 0
        self.MDBusyTime = []

        self.DLServers = []
        self.DLServerQueue = deque()
        self.DLServerQueueLengths = []
        self.DLwaitTime = 0
        # Used for graph tracking/generation
        self.DLmaxQueueLength = 0
        self.DLBusyTime = []

        self.VRServers = []
        self.VRServerQueue = deque()
        self.VRServerQueueLengths = []
        self.VRwaitTime = 0
        # Used for graph tracking/generation
        self.VRmaxQueueLength = 0
        self.VRBusyTime = []

        self.BOServers = []
        self.BOServerQueue = deque()
        self.BOServerQueueLengths = []
        self.BOwaitTime = 0
        # Used for graph tracking/generation
        self.BOmaxQueueLength = 0   
        self.BOBusyTime = []

        # Service all queues
        for i in range(self.numMD):
            self.MDServers.append(MainDesk.MainDesk(self.mdm, self.mdM, 'MD' + str(i)))
            self.MDBusyTime.append(0)

        for i in range(self.numDL):
            self.DLServers.append(Server.Server(self.dlm, self.dlM, 'DL' + str(i)))
            self.DLBusyTime.append(0)

        for i in range(self.numVR):
            self.VRServers.append(Server.Server(self.vrm, self.vrM, 'VR' + str(i)))
            self.VRBusyTime.append(0)

        for i in range(self.numBO):
            self.BOServers.append(Server.Server(self.bom, self.boM, "BO" + str(i)))
            self.BOBusyTime.append(0)

    
    def printAllServerTimes(self):

        for i in range(self.numMD):
            self.MDServers[i].printServerTimes()

        for i in range(self.numDL):
            self.DLServers[i].printServerTimes()

        for i in range(self.numVR):
            self.VRServers[i].printServerTimes()

        for i in range(self.numBO):
            self.BOServers[i].printServerTimes()

    def printAllDistributions(self):

        for i in range(self.numMD):
            self.MDServers[i].printDistribution()

        for i in range(self.numDL):
            self.DLServers[i].printDistribution()

        for i in range(self.numVR):
            self.VRServers[i].printDistribution()

        for i in range(self.numBO):
            self.BOServers[i].printDistribution()
        


    def printAllAverageTimes(self):
        
        for i in range(self.numMD):
            self.MDServers[i].printDistribution()

        for i in range(self.numDL):
            self.DLServers[i].printAverageServeTime()

        for i in range(self.numVR):
            self.VRServers[i].printAverageServeTime()

        for i in range(self.numBO):
            self.BOServers[i].printAverageServeTime()
        

    def printAllServedCustomerPerServer(self):

        for i in range(self.numMD):
            self.MDServers[i].printCustomersServed()

        for i in range(self.numDL):
            self.DLServers[i].printCustomersServed()

        for i in range(self.numVR):
            self.VRServers[i].printCustomersServed()

        for i in range(self.numBO):
            self.BOServers[i].printCustomersServed()

    def printMaxQueueLength(self):
        print("Maximum Queue length reached for all queues, [MD, DL, VR, BO] = [%d, %d, %d, %d]" % (self.MDmaxQueueLength, self.DLmaxQueueLength, self.VRmaxQueueLength, self.BOmaxQueueLength))


    def incrementWaitTime(self):
        self.MDwaitTime += len(self.MDServerQueue)
        self.DLwaitTime += len(self.DLServerQueue)
        self.VRwaitTime += len(self.VRServerQueue)
        self.BOwaitTime += len(self.BOServerQueue)

    def generateWaitAndUtilizationTimeNow(self):

        ### Wait Times ###
        holder = (self.MDwaitTime / self.simClock)
        self.MDServerQueueLengths.append(holder)

        holder = (self.DLwaitTime / self.simClock)
        self.DLServerQueueLengths.append(holder)

        holder = (self.VRwaitTime / self.simClock)
        self.VRServerQueueLengths.append(holder)

        holder = (self.BOwaitTime / self.simClock)
        self.BOServerQueueLengths.append(holder)


        ### Utilization Times ###

        for i in range(self.numMD):
            holder = (self.MDBusyTime[i] / self.simClock)
            self.MDServers[i].appendUtilTimes(holder)

        for i in range(self.numDL):
            holder = (self.DLBusyTime[i] / self.simClock)
            self.DLServers[i].appendUtilTimes(holder)

        for i in range(self.numVR):
            holder = (self.VRBusyTime[i] / self.simClock)
            self.VRServers[i].appendUtilTimes(holder)

        for i in range(self.numBO):
            holder = (self.BOBusyTime[i] / self.simClock)
            self.BOServers[i].appendUtilTimes(holder)

        self.timePoints.append(self.simClock)


        ### Debug function ###
    def printWaitTimes(self):
        print(self.MDServerQueueLengths)
        print(self.DLServerQueueLengths)
        print(self.VRServerQueueLengths)
        print(self.BOServerQueueLengths)

        print(len(self.MDServerQueueLengths))
        print(len(self.DLServerQueueLengths))
        print(len(self.VRServerQueueLengths))
        print(len(self.BOServerQueueLengths))
        print(len(self.timePoints))

        ### Debug Function ###
    # def printUtilTimes(self):
    #     print(self.MDBusyTimeList)
    #     print(self.DLBusyTimeList)
    #     print(self.VRBusyTimeList)
    #     print(self.BOBusyTimeList)        


    def generateAverageQueueWaitTimeGraph(self,simNum):

        name = 'Average Wait Time (Main Desk)'
        plt.plot(self.MDServerQueueLengths)
        plt.title(name)
        l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
        l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
        plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.xlabel("time(m)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(simNum) + "_for_MD.png", bbox_inches='tight')
        plt.clf()

        name = 'Average Wait Time (Drivers License)'
        plt.plot(self.DLServerQueueLengths)
        plt.title(name)
        l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
        l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
        plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.xlabel("time(m)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(simNum) + "_for_DL.png", bbox_inches='tight')
        plt.clf()

        name = 'Average Wait Time (Vehicle Registration)'
        plt.plot(self.VRServerQueueLengths)
        plt.title(name)
        l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
        l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
        plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.xlabel("time(m)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(simNum) + "_for_VR.png", bbox_inches='tight')
        plt.clf()

        name = 'Average Wait Time (Both)'
        plt.plot(self.BOServerQueueLengths)
        plt.title(name)
        l1 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
        l2 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')
        plt.legend(handles = [l1, l2], loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.xlabel("time(m)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(simNum) + "_for_BO.png", bbox_inches='tight')
        plt.clf()

        name = 'Average Wait Time (All Queues)'
        l1, = plt.plot(self.MDServerQueueLengths, label="Main Deak")
        l2, = plt.plot(self.DLServerQueueLengths, label="Driver License" )
        l3, = plt.plot(self.VRServerQueueLengths, label="Vehicle Registration")
        l4, = plt.plot(self.BOServerQueueLengths, label="Both")
        l5 = plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)')
        l6 = plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)')

        plt.xlim([0,500])
        plt.legend(handles = [l1, l2, l3, l4, l5, l6], loc='upper center', bbox_to_anchor=(0.5,-0.1))
        plt.title(name)
        plt.xlabel("time(m)")
        plt.ylabel("Average Wait Time")
        plt.savefig("Sim_" + str(simNum) + "_for_all.png", bbox_inches='tight')
        plt.clf()

    def generateServerUtilization(self, simNum):

        name = 'Server Utilization'
        lists = []

        for i in range(self.numMD):
            l1, = plt.plot(self.MDServers[i].getUtilTimes(), label="Main Desk")
            lists.append(l1)

        for i in range(self.numDL):
            l2, = plt.plot(self.DLServers[i].getUtilTimes(), label="Driver License " + self.DLServers[i].getServerID())
            lists.append(l2)

        for i in range(self.numVR):
            l3, = plt.plot(self.VRServers[i].getUtilTimes(), label="Vehicle Registration " + self.VRServers[i].getServerID())
            lists.append(l3)

        for i in range(self.numBO):
            l4, = plt.plot(self.BOServers[i].getUtilTimes(), label="Both " + self.BOServers[i].getServerID())
            lists.append(l4)

        lists.append(plt.axvline(x=self.opens, color='b', label='PRE CLOSE (7.5 hrs)'))
        lists.append(plt.axvline(x=self.closes, color='r', label='CLOSED (8 hrs)'))
        plt.xlim([0,500])
        plt.legend(handles = lists)
        plt.legend(handles= lists, loc='upper center', bbox_to_anchor=(0.5,-0.1))
        # plt.legend(handles= lists, bbox_to_anchor=(0, 1), loc='upper left', ncol=1)
        plt.title(name)

        plt.xlabel("time(m)")
        plt.ylabel("Utilization (%)")
        plt.savefig("Sim_Util_" + str(simNum) + "_for_all.png", bbox_inches='tight')

        plt.clf()



    def startSim(self, name):

        # print(self.arrivalTimes) # Testing times, functions correctly. 

        myIter = 0 
        served = 0

        # print(self.custArrival)

        while 1:

            # print("\nTime = %d" %(self.simClock))

            self.incrementWaitTime()
            for i in range(self.numMD):
                MDresult = self.MDServers[i].serveTheCustomer(self.simClock)

                if MDresult[0] != 0 and MDresult[1] != 0:
                    self.MDBusyTime[i] += 1 

                if MDresult[2] == 'DL Queue':
                    # print('dl queue')
                    # print(MDresult)
                    self.DLServerQueue.append(MDresult)
                    # print("appending to DL, new size %d." % (len(self.DLServerQueue)))
                    if self.DLmaxQueueLength < len(self.DLServerQueue):
                        self.DLmaxQueueLength = len(self.DLServerQueue)

                elif MDresult[2] == 'VR Queue':
                    # print('vr queue')
                    # print(MDresult)
                    self.VRServerQueue.append(MDresult)
                    # print("appending to VR, new size %d." % (len(self.VRServerQueue)))
                    if self.VRmaxQueueLength < len(self.VRServerQueue):
                        self.VRmaxQueueLength = len(self.VRServerQueue)
                    

                elif MDresult[2] == 'BO Queue':
                    # print('bo queue')
                    # print(MDresult)
                    self.BOServerQueue.append(MDresult) 
                    # print("appending to BO, new size %d." % (len(self.BOServerQueue)))
                    if self.BOmaxQueueLength < len(self.BOServerQueue):
                        self.BOmaxQueueLength = len(self.BOServerQueue) 
                

            # Service all queues
            for i in range(self.numDL):
                self.DLBusyTime[i] += self.DLServers[i].serveTheCustomer()

            for i in range(self.numVR):
                self.VRBusyTime[i] += self.VRServers[i].serveTheCustomer()

            for i in range(self.numBO):
                self.BOBusyTime[i] += self.BOServers[i].serveTheCustomer()


            ### Add new customers to the main queue ### 
            if self.custArrival[myIter] == self.simClock:
                self.MDServerQueue.append([self.custArrival[myIter], 'c'+str(myIter), 'arr'])
                # self.queueLengths.append(len(self.MDServerQueue))

                if self.MDmaxQueueLength < len(self.MDServerQueue):
                    self.MDmaxQueueLength = len(self.MDServerQueue)

                myIter += 1
                if myIter == self.totalCustomers:
                    myIter -= 1 # avoids out of bound access

            for i in range(self.numMD):
                if (not self.MDServers[i].getBusyState() and len(self.MDServerQueue) > 0):
                    customer = self.MDServerQueue.popleft()
                    start, stop = self.MDServers[i].service(self.simClock, customer)
                    # print(customer)
                    # print(start)
                    # print(stop)
                    # self.FEL.pushEvent(start)
                    # self.FEL.pushEvent(stop)
                    self.MDServers[i].serveTheCustomer(self.simClock)
                    self.MDBusyTime[i] += 1

            for i in range(len(self.DLServers)):
                if (not self.DLServers[i].getBusyState() and len(self.DLServerQueue) > 0):
                    # print('\n')
                    customer = self.DLServerQueue.popleft()
                    start, stop = self.DLServers[i].service(self.simClock, customer)
                    # print(customer)
                    # print(start)
                    # print(stop)
                    # self.FEL.pushEvent(start)
                    # self.FEL.pushEvent(stop)
                    self.DLBusyTime[i] += self.DLServers[i].serveTheCustomer()
                    # print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.DLServers[i].getServerID()))
                    served += 1

            for i in range(len(self.VRServers)):
                if (not self.VRServers[i].getBusyState() and len(self.VRServerQueue) > 0):
                    # print('\n')
                    customer = self.VRServerQueue.popleft()
                    start, stop = self.VRServers[i].service(self.simClock, customer)
                    # print(customer)
                    # print(start)
                    # print(stop)
                    # self.FEL.pushEvent(start)
                    # self.FEL.pushEvent(stop)
                    self.VRBusyTime[i] += self.VRServers[i].serveTheCustomer()
                    # print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.VRServers[i].getServerID()))
                    served += 1

            for i in range(len(self.BOServers)):
                if (not self.BOServers[i].getBusyState() and len(self.BOServerQueue) > 0):
                    # print('\n')
                    customer = self.BOServerQueue.popleft()
                    start, stop = self.BOServers[i].service(self.simClock, customer)
                    # print(customer)
                    # print(start)
                    # print(stop)
                    # self.FEL.pushEvent(start)
                    # self.FEL.pushEvent(stop)
                    self.BOBusyTime[i] += self.BOServers[i].serveTheCustomer()
                    # print("Server %s is FINALLY DOING SOMETHING USEFUL!!!" %(self.BOServers[i].getServerID()))
                    served += 1

            # print('\n')
            # print("MD server queue = %d" %(len(self.MDServerQueue)))
            # print("DL server queue = %d" %(len(self.DLServerQueue)))
            # print("VR server queue = %d" %(len(self.VRServerQueue)))
            # print("BO server queue = %d" %(len(self.BOServerQueue)))

            self.generateWaitAndUtilizationTimeNow()
            time.sleep(.000000001)
            self.simClock += 1

            mdsNotBusy = 0
            dlsNotBusy = 0
            vrsNotBusy = 0
            bosNotBusy = 0

            for i in range(self.numMD):
                if not self.MDServers[i].getBusyState():
                    mdsNotBusy += 1

            for i in range(self.numDL):
                if not self.DLServers[i].getBusyState():
                    dlsNotBusy += 1

            for i in range(self.numVR):
                if not self.VRServers[i].getBusyState():
                    vrsNotBusy += 1

            for i in range(self.numBO):
                if not self.BOServers[i].getBusyState():
                    bosNotBusy += 1
            if (dlsNotBusy == self.numDL and vrsNotBusy == self.numVR and bosNotBusy == self.numBO and served == self.totalCustomers):
                # self.printAllServerTimes()
                # self.printAllAverageTimes()
                # self.printAllDistributions()
                self.printAllServedCustomerPerServer()
                print("Total Customers Processed = %d at time %d(minutes)." %(served, self.simClock))
                self.printMaxQueueLength()
                self.generateAverageQueueWaitTimeGraph(name)
                self.generateServerUtilization(name)
                # print(self.VRBusyTimeList[0])
                # self.printWaitTimes()
                # self.printUtilTimes()
                break
            # if (not self.server1.getBusyState() and not self.server2.getBusyState() and self.servedCustomers == self.totalCustomers):
            #     break



