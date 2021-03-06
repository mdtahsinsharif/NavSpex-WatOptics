from threading import Thread
from multiprocessing import Process, Value, Lock
from Software.RouteFinding.PictureProcessing import pp_module as pp
import threading
import importlib
import sys
import os
import thread_navigation
# import thread_obstacle
import time
import Software.WatOptics_firmware.hardware_testing.IMU.wiringPi.LSM9DS1_RaspberryPi_Library.example.LSM9DS1_Basic_I2C as imu_module
import Software.WatOptics_firmware.hardware_testing.Sonar.rangeFind as sonar_thread

if __name__ == "__main__":
    triangleIds = pp.LoadData("Software/RouteFinding/Data/symposium_map.jpg")

    v = Value('i', 0)
    imu_counter = Value('i', 0)
    obstacle_detected = Value('i', 0)
    imu_direction = Value('i', 0)
    obstacle_value = Value('i',9999)
    camera_bool = Value('i',0)
    lock = Lock()
    procs = []
    procs.append(Process(target=thread_navigation.thread_navigate, args=(v,lock, triangleIds, imu_counter, imu_direction, obstacle_detected, camera_bool)))
    procs.append(Process(target=imu_module.imu_step_counter, args=(imu_counter,imu_direction)))
    procs.append(Process(target=sonar_thread.sonar_detect, args=(obstacle_value,obstacle_detected, camera_bool)))

    for p in procs: p.start()
    for p in procs: p.join()
    #thread_navigation.DemoButtonInput();
