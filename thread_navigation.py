import sys
import os
import time
import RPi.GPIO as GPIO

import Software.WatOptics_firmware.hardware_testing.barcode_scanner.barcode_scanner_video as bsv
import Software.RouteFinding.UserInterfacing.ui_module as ui
import Software.RouteFinding.PathFinding.pf_module as pf
import Software.RouteFinding.Data.e5_4f as d ## this needs to be done based on input

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 18 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 22 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 24 to be an input pin and set initial value to be pulled low (off)


def getRoomNumber():
    thousands = 4
    hundreds = 0
    tens = 0
    ones = 0


    while True: # Run forever
        if GPIO.input(16) == GPIO.HIGH:
            
            #roomNumber = 4008
        
            hundreds += 1
            if (hundreds > 9):
                hundreds = 0
            ui.SpeakCommand(str(hundreds))
            time.sleep(0.3)
            
        if GPIO.input(18) == GPIO.HIGH:
            
            #roomNumber = 4037
            
            tens += 1
            if (tens > 9):
                tens = 0
            ui.SpeakCommand(str(tens))
            time.sleep(0.3)
            
        if GPIO.input(22) == GPIO.HIGH:
            
            #roomNumber = 4032
            
            ones += 1
            if (ones > 9):
                ones = 0
            ui.SpeakCommand(str(ones))
            time.sleep(0.3)
        
        if GPIO.input(24) == GPIO.HIGH:
        
            #roomNumber = 4118
        
            print("EXIT BUTTON")
            break
            
    roomNumber = (thousands * 1000) + (hundreds * 100) + (tens * 10) + ones

    thousand_s = str(thousands) + ' '
    hundred_s = str(hundreds) + ' '
    ten_s = str(tens) + ' '
    one_s = str(ones) + ' '

    roomNumber_s = thousand_s + hundred_s + ten_s + one_s

    ui.SpeakCommand("Confirm room number: " + roomNumber_s)
    print(roomNumber)
    return str(roomNumber)

def GetCameraInput(lock):
        ui.SpeakCommand("Determining! current! location, please! stay! steady!")
        with lock:
               camera_return = bsv.scan_barcode()
        return camera_return

def thread_navigate(shared_val,lock, tIds, num_steps, imu_direction, obs):
    rerun_astar = False
    keepRunning = 0
    start_prog = False
    ##camera_return = -1
    while keepRunning < 3:
        ## wait for button to start 
        '''# ------ Insert Code here ----- #'''
        ui.SpeakCommand("Please press any button to begin")
        
        while start_prog == False:
        # might need to add delay here and in room input for SONAR
            if GPIO.input(16) == GPIO.HIGH or GPIO.input(18) == GPIO.HIGH or GPIO.input(22) == GPIO.HIGH or GPIO.input(24) == GPIO.HIGH:
                start_prog = True
        '''# ------ End here ----- #'''

        
        ## Get current location
        '''# ------ Insert Code here ----- #'''
        ## 1. Use camera to detect current location
        ## 2. Ask user to input the room
        # ui.SpeakCommand("Determining! current! location, please! stay! steady!")
        # with lock:
        #        camera_return = bsv.scan_barcode()
        camera_return = "-1"
        
        #camera_return = GetCameraInput(lock)
        
        print("[thread_navigate] camera", camera_return)

        if camera_return != "-1":
                s = camera_return
        else:
                ui.SpeakCommand("Please enter current room")
                s = getRoomNumber()
        '''# ------ End here ----- #'''

        ## Get destination
        if rerun_astar == False:
            '''# ------ Insert Code here ----- #'''
            ui.SpeakCommand("Please enter destination room")
            #e = "4007"
            e = getRoomNumber()
            '''# ------ End here ----- #'''

        ## Map start and end to coordinates:
        ## make sure room numbers are valid TODO
        start = d.rooms[s][0] ## returns a list, take first value
        end = d.rooms[e][0]

        ## Run A* 
        coordinates, _, _ = pf.FindPath(tIds, start, end)
        instructions = pf.GetInstructions(coordinates, d.mapScale*d.strideMen)
        rerun_astar = False ## got new path, astar = false
        direction = True
        required_direction = 0
        imu_direction.value = 0
        obs.value = 0
        for inst in instructions:
                ## send instruction
                command = ui.GenerateWalkCommand(inst)
                print(command)
                ui.SpeakCommand(command)
                required_direction = inst[0]
                required_steps = inst[1]

                num_steps.value = 0
                while direction == True and num_steps.value < required_steps:
                        ##  Count Steps, Check direction
                        '''# ------ Insert Code here ----- #'''
                        # steps_counter = num_steps
                        if obs.value:
                            ui.SpeakCommand("Obstacle detected")
                            obs.value = 0
                            time.sleep(0.2)
                        print("[thread_navigation]: steps required: ", required_steps)
                        print("[thread_navigation]: steps taken:", num_steps.value)
                        time.sleep(0.3)
                        ## Direction = true if moving in the true_direction
                        print("[thread_navigation]: required_direction: ", required_direction)
                        print("[thread_navigation]: imu_direction: ", imu_direction.value)
                        if required_direction == imu_direction.value:
                                direction = True
                                imu_direction.value = 0
                                required_direction = 0
                        else:
                                ui.SpeakCommand("You turned the wrong direction! Rerouting.")
                                direction = False
                                
                        '''# ------ End here ----- #'''

                ## Turned the wrong way?
                if direction == False:
                        ## they changed direction, rerun A*
                        rerun_astar = True
                        start_prog = True
                        break
        
        if rerun_astar == True:
                ## ignore the rest of the loop and start over
                keepRunning += 1
                continue

        ## Start camera
        '''# ------ Insert Code here ----- #'''
        ## start camera and detect whether destination reached
        
        #camera_input = GetCameraInput(lock)
        camera_input = camera_return
        if camera_input == camera_return:
                ui.SpeakCommand("Destination is infront of you.")
                start_prog = False
        ##'''# ------ End here ----- #'''
        else:
                rerun_astar = True
                start_prog = True
        
        keepRunning += 1