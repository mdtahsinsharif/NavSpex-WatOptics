import threading
from threading import Thread
import importlib
import sys
import os
#sys.path.insert(0, os.getcwd() + '/Software/WatOptics_firmware/hardware_testing/Sonar')
#import rangeFind
import subprocess
import time
import xlwt 
from xlwt import Workbook 

SONAR_THRESHOLD = 330
isObstaclePresent = False
sonarVal_s = ""
sonarVal_i = 5000


#def checkSonarVal (sonarData):
#    global sonarVal_s
#    global sonarVal_i 
#    sonarVal_s = sonarData.read()
#		
#    if (sonarVal_s != "")
#	sonarVal_i = int(sonarVal_s)
#
#    return sonarVal_i
#	
#def checkObstaclePresent (sonarVal_i):
#	
#    if (sonarVal_i < threshold):
#	return True
#	
#    return False

def thread_obstacle_detection(shared_val, lock, obstacle_detect_bool):
    subprocess.call(["sudo",  "python3",  "./Software/WatOptics_firmware/hardware_testing/Sonar/rangeFind.py"])
    
    #wb = Workbook() 
    #sheet1 = wb.add_sheet('Sonar_csv.csv')
    #sheet1.write(0,0,320)
    val = 320
    while True:
        
        print("[thread_obstacle_detection] before while loop")
        if time.localtime().tm_sec % 2 == 1:
            sonarFile = open("Sonar.txt", "r")
            proximity = sonarFile.read()
            if int(proximity) <= SONAR_THRESHOLD:
                obstacle_detect_bool = 1
                print("[thread_obstacle_detection]: time: ", time.localtime().tm_sec)
                print("[thread_obstacle_detection]: Sonar value: ", proximity)
                #subprocess.call(["espeak", "Obstacle detected ahead! Please take precautionary measure"])
                time.sleep(5)
            sonarFile.close()
            
        if time.localtime().tm_sec % 2 == 3:
            writeFile = open("Sonar1.txt", "w")
            val = val+1
            writeFile.write(str(val))
            writeFile.close()
            #val = val+1
           # print(" should write ", val)
#            sheet1.write(0, 0, val)
        
	
    ##rangeFind.sonar_detect();
    print("[thread_obstacle_detection] end")