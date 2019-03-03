import threading
from threading import Thread
import importlib
import sys
import os
import thread_navigation
import thread_obstacle

def func1():
    threadlock.acquire()
    print('Working1')
    threadlock.release()
    ##working
print(os.getcwd())
threadlock = threading.Lock()
threads = []

Thread(target = thread_obstacle.thread_obstacle_detection()).start()
Thread(target = thread_navigation.thread_navigate()).start()
