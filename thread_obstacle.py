import threading
from threading import Thread
import importlib
import sys
import os
sys.path.insert(0, os.getcwd() + '/Software/WatOptics_firmware/hardware_testing/Sonar')
#import rangeFind
import subprocess
import time

def thread_obstacle_detection(shared_val, lock):
    #subprocess.call(["sudo",  "python3",  "./Software/WatOptics_firmware/hardware_testing/Sonar/rangeFind.py"])
    ##rangeFind.sonar_detect();
    print("[thread obstacle detection] starting:")
    shared_val.value = 0
    #print("Before while in t1")
    while shared_val.value==0:
        #with lock:
        print("[thread_obstacle_detection] running:")
        time.sleep(1)
    print("[thread_obstacle_detection] end:")