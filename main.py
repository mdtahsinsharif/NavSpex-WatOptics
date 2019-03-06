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
import Software.WatOptics_firmware.hardware_testing.Sonar.rangeFind as sonar_thread

if __name__ == "__main__":
    triangleIds = pp.LoadData("Software/RouteFinding/Data/e5_4f.jpg")

    v = Value('i', 0)
    imu_counter = Value('i', 0)
    obstacle_detected = Value('i', 0)
    imu_direction = Value('i', 0)
    obstacle_value = Value('i',9999)
    lock = Lock()
    procs = []
    procs.append(Process(target=thread_navigation.thread_navigate, args=(v,lock, triangleIds, imu_counter, imu_direction, obstacle_detected)))
    procs.append(Process(target=imu_module.imu_step_counter, args=(imu_counter,imu_direction)))
	#procs.append(Process(target=thread_obstacle.thread_obstacle_detection, args=(v,lock, obstacle_detected, obstacle_value)))
    procs.append(Process(target=sonar_thread.sonar_detect, args=(obstacle_value,obstacle_detected)))

    for p in procs: p.start()
    for p in procs: p.join()


