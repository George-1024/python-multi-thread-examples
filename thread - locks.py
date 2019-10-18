import threading
import time
#Thread lock
LOCK = threading.Lock()
class MyThread(threading.Thread):
    "A derived class which customizes the thread.run method"
    def __init__(self,name,delay):
        threading.Thread.__init__(self) #call base constructor
        self._name = name
        self._delay = delay

    def run(self):
        for i in range(5):
            LOCK.acquire()
            print("Hello From %s - %s" % (self._name,time.ctime()))
            LOCK.release()
            time.sleep(self._delay)
# Create Our Threads
a = MyThread("Thread A",1)
b = MyThread("Thread B",2)
# Start Our Threads
a.start()
b.start()
# Wait for them both to finish
a.join()
b.join()
#Terminate Message
print("Terminated")

