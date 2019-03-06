import threading
from threading import Thread
import importlib
import sys
import os
import subprocess
import time
import xlwt 
from xlwt import Workbook 

SONAR_THRESHOLD = 330

def thread_obstacle_detection(shared_val, lock, obstacle_detected, obstacle_value):
    val = True
    while val==True:
        print("[thread_obstacle_detection]: Sonar value: ", obstacle_value.value)
        if obstacle_value.value <= SONAR_THRESHOLD:
            obstacle_detected.value = 1
            print("[thread_obstacle_detection]: BELOW THRESHOLD Sonar value: ", obstacle_value.value)
            print("[thread_obstacle_detection]: Wait since obstacle ")
            time.sleep(2)
            #val = False
        time.sleep(0.5)
        print("[thread_obstacle_detection] obstacle_detected: ", obstacle_detected.value)
          
    print("[thread_obstacle_detection] end")