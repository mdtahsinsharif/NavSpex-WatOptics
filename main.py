from threading import Thread
from multiprocessing import Process, Value, Lock
from Software.RouteFinding.PictureProcessing import pp_module as pp
import threading
import importlib
import sys
import os
import thread_navigation
import thread_obstacle
import time

if __name__ == "__main__":
    triangleIds = pp.LoadData("Software/RouteFinding/Data/e5_4f.jpg")

    v = Value('i', 0)
    lock = Lock()
    procs = [Process(target=thread_navigation.thread_navigate, args=(v,lock, triangleIds))]
    #procs[0].start()
    procs.append(Process(target=thread_obstacle.thread_obstacle_detection, args=(v,lock)))
    #procs[1].start()

    for p in procs: p.start()
    for p in procs: p.join()


