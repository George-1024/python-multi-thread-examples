from queue import Queue
import math, threading, time
#Queue
QUEUE = Queue()
_sentinel = object() # object which causes it to quit
class Producer(threading.Thread):
    "Producer: Produces Sensor Measurements"
    def run(self):
        for i in range(359):
            QUEUE.put(math.sin(i*math.pi/180.0)) # generate sensor measurement
            time.sleep(0.01)
            QUEUE.put(_sentinel)
class Consumer(threading.Thread):
    "Consumer: Performs Post Processing"
    def run(self):
        while True:
            data = QUEUE.get(timeout=2) # receive measurement from sensor thread
            if data is _sentinel:
                break
            else:
                print("Data: %f" % data) # process measurement

# Create Our Threads
P = Producer()
C = Consumer()
# Start Our Threads
C.start()
P.start()
# Wait for Threads to End
P.join()
C.join()
#Terminate Message
print("Terminated")
