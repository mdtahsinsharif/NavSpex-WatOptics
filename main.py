import threading
from threading import Thread
import importlib
import sys
import os
import thread_navigation

def func1():
    threadlock.acquire()
    print('Working1')
    threadlock.release()
    
print(os.getcwd())
threadlock = threading.Lock()
threads = []

Thread(target = func1).start()
Thread(target = thread_navigation.thread_navigate()).start()
