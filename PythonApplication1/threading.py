import time

# synchronous : takes 25 sec
def long_task():
    for i in range(5):
        time.sleep(1)
        print ("workingL %s\n" %i)

print ("start")

for i in range(5):
    long_task()

print("end")

# asynchronous using thread : takes 5 sec
import threading
def long_task_async():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task_async)  # create thread
    threads.append(t)

for t in threads:
    t.start()  # run thread

for t in threads:
    t.join()  # join : wait for one thread to be finished

print("End")
