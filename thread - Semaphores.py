import threading, time
#Thread lock + Semaphore
LOCK = threading.Lock()
SEM = threading.BoundedSemaphore(value=2)
class MyThread(threading.Thread):
    "A derived class which customizes the thread.run method"
    def __init__(self,name):
        threading.Thread.__init__(self) #call base constructor
        self._name = name

    def run(self):
        for i in range(5):
            #Acquire Semaphore
            SEM.acquire()
            #Do some work
            LOCK.acquire()
            print("Doing Work in Thread %s" % self._name)
            LOCK.release()
            time.sleep(1)
            #Release Semaphore
            SEM.release()
# Create Our Threads
a = MyThread("Thread A")
b = MyThread("Thread B")
c = MyThread("Thread C")
# Start Our Threads
a.start()
b.start()
c.start()
# Wait for them all to finish
a.join()
b.join()
c.join()
#Terminate Message
print("Terminated")

