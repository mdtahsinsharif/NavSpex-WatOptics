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
import Software.WatOptics_firmware.hardware_testing.IMU.wiringPi.LSM9DS1_RaspberryPi_Library.example.LSM9DS1_Basic_I2C as imu_module

if __name__ == "__main__":
    triangleIds = pp.LoadData("Software/RouteFinding/Data/e5_4f.jpg")

    v = Value('i', 0)
    imu_counter = Value('i', 0)
    lock = Lock()
    procs = [Process(target=thread_navigation.thread_navigate, args=(v,lock, triangleIds, imu_counter))]
    #procs.append(Process(target=thread_obstacle.thread_obstacle_detection, args=(v,lock)))
    procs.append(Process(target=imu_module.imu_step_counter, args=(imu_counter,)))


    for p in procs: p.start()
    for p in procs: p.join()


