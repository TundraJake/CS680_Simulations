import time # Used for the clock (seconds).
import Server
import Customers
from collections import deque

### Clock code from following link, 
### http://codereview.stackexchange.com/questions/26534/is-there-a-better-way-to-count-seconds-in-python
###
class Simulation():

    def __init__(self, s1m, s1M, s2m, s2M, numCust, cAm, cAM):

        self.simClock = 0
        self.server1 = Server.Server(s1m, s1M)
        self.server1ServerTimes = []

        self.server2 = Server.Server(s2m, s2M)
        self.server2ServerTimes = []

        self.averageWaitTime = 0

        self.custs = Customers.Customers(numCust, cAm, cAM)
        self.lastCustomerTime = self.custs.getLastCustomerTime()

    def toggleServerBusyState(self):
        if self.server1.getBusyState():
            print("The server is now busy!")
        else:
            print("Why we pay you") 


    def startSim(self, seconds):

        start = time.time()
        # time.time() returns the number of seconds since the unix epoch.
        # To find the time since the start of the function, we get the start
        # value, then subtract the start from all following values.
        time.clock()    
        # When you first call time.clock(), it just starts measuring
        # process time. There is no point assigning it to a variable, or
        # subtracting the first value of time.clock() from anything.
        # Read the documentation for more details.

        print(self.custs.getAllCustomers())

        myIter = 0 
        # firstValue = self.custs.getCurrentCustomer(0)
        # print("%d is the first values" % (firstValue))
        while self.simClock < seconds:
            # self.simClock = time.time() - start
            # print("loop cycle time: %f, seconds count: %02d" % (time.clock() , self.simClock)) 


            self.simClock += 1

            if self.simClock == self.custs.getCurrentCustomer(myIter):
                print("assign customer to server now")
                myIter += 1

            else:
                print("It is not working")



            time.sleep(.5)  




            # You were sleeping in your original code, so I've stuck this in here...
            # You'll notice that the process time is almost nothing.
            # This is because we are spending most of the time sleeping,
            # which doesn't count as process time.
            # For funsies, try removing "time.sleep()", and see what happens.
            # It should still run for the correct number of seconds,
            # but it will run a lot more times, and the process time will
            # ultimately be a lot more. 
            # On my machine, it ran the loop 2605326 times in 20 seconds.
            # Obviously it won't run it more than 20 times if you use time.sleep(1)
