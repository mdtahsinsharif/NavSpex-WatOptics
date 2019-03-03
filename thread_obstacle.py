import threading
from threading import Thread
import importlib
import sys
import os
sys.path.insert(0, os.getcwd() + '/Software/WatOptics_firmware/hardware_testing/Sonar')
#import rangeFind
import subprocess

def thread_obstacle_detection():
    subprocess.call(["sudo",  "python3",  "./Software/WatOptics_firmware/hardware_testing/Sonar/rangeFind.py"])
    ##rangeFind.sonar_detect();
    print("Thread obstacle detection.")