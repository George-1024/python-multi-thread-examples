import threading, time
#Thread lock + Condition
LOCK = threading.Lock()
COND = threading.Condition()
class Producer(threading.Thread):
    "Producer: Produces Sensor Measurements"
    def run(self):
        for i in range(5):
            COND.acquire() #acquire condition
            COND.notifyAll() #inform other thread(s) we have a reading
            COND.release() #release it
            LOCK.acquire()
            print("Produced a Reading")
            LOCK.release()
            time.sleep(1)
class Consumer(threading.Thread):
    "Consumer: Performs Post Processing"
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True
    def terminate(self):
        self._running = False
        def run(self):
            while self._running:
                COND.acquire() #acquire the condition in this thread
                gotit = COND.wait(2) # wait for reading with 2 second time out
                COND.release() #release it
                if(gotit):
                    LOCK.acquire()
                    print("Consumed a Reading")
                    LOCK.release()
# Create Our Threads
P = Producer()
C = Consumer()
# Start Our Threads
C.start()
P.start()
# Wait for producer to end
P.join()
# Terminate our consumer
C.terminate()
C.join()
#Terminate Message
print("Terminated")

