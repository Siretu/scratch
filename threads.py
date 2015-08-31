import thread
from time import sleep

def thread_fun(thread_name):
    i = 0
    while 1:
        print "%s: %d" % (thread_name, i)
        i += 1
        sleep(0.1)


thread.start_new_thread(thread_fun,("Thread 1",))
thread.start_new_thread(thread_fun,("Thread 2",))

while 1:
    pass
