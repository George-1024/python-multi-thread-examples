import threading, datetime, time
#Our Customized Thread Class
class TaskThread(threading.Thread):
    """Thread that executes a task every N seconds"""

    def __init__(self):
        threading.Thread.__init__(self) #call base constructor
        self._finished = threading.Event() #Event object
        self._interval = 1.0 #default interval

    def setInterval(self, interval):
        """Set the number of seconds we sleep between executing our task"""
        self._interval = interval

    def shutdown(self):
        """Stop this thread"""
        self._finished.set()

    def run(self):
        while 1:
            if self._finished.isSet(): return
            print("Hello at time: " + str(datetime.datetime.now()))

            # sleep for interval or until shutdown
            self._finished.wait(self._interval)
#Our Derived Class
class MyEvent(TaskThread):
    """Execution every N seconds"""
    def task(self):
        print("Hello at time: " + str(datetime.datetime.now()))

#Try It
ME = MyEvent()
ME.setInterval(0.5)
ME.start()
while True:
    try:
        time.sleep(1)
        print("Hello from while loop!")
    except KeyboardInterrupt:
        ME.shutdown()
        break

