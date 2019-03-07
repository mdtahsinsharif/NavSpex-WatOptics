import Software.RouteFinding.PictureProcessing.pp_module as pp
from Software.RouteFinding.PictureProcessing import opencv_wrapper as wcv2
from Software.RouteFinding.PathFinding import pf_module as pf
from Software.RouteFinding.UserInterfacing import ui_module as ui
from Software.RouteFinding.Data import e5_4f as d ## TODO: Figure out how to change this based on user input

def Nav_Thread(tIds):
    rerun_astar = False
    keepRunning = 0
    while keepRunning < 3:
        ## wait for button to start 
        '''# ------ Insert Code here ----- #'''

        '''# ------ End here ----- #'''

        
        ## Get current location
        '''# ------ Insert Code here ----- #'''
        ## 1. Use camera to detect current location
        ## 2. Ask user to input the room
        camera_return = "4020"
        if camera_return != "-1":
                s = camera_return
        else:
                s = "4020"
        '''# ------ End here ----- #'''

        ## Get destination
        if rerun_astar == False:
            '''# ------ Insert Code here ----- #'''
            ui.SpeakCommand("Please enter destination room")
            e = "4117"
            ui.SpeakCommand("Confirm destination: " + e)
            '''# ------ End here ----- #'''

        ## Map start and end to coordinates:
        start = d.rooms[s][0] ## returns a list, take first value
        end = d.rooms[e][0]

        ## Run A* 
        coordinates, _, _ = pf.FindPath(tIds, start, end)
        instructions = pf.GetInstructions(coordinates, d.mapScale*d.strideMen)
        rerun_astar = False ## got new path, astar = false
        
        for inst in instructions:
                ## send instruction
                command = ui.GenerateWalkCommand(inst)
                ui.SpeakCommand(command)
                true_direction = inst[0]
                num_steps = inst[1]

                direction = True
                steps_counter = 0
                while direction == True and steps_counter < num_steps:
                        ##  Count Steps, Check direction
                        '''# ------ Insert Code here ----- #'''
                        steps_counter = num_steps

                        ## Direction = true if moving in the true_direction
                        direction = True
                        '''# ------ End here ----- #'''

                ## Turned the wrong way?
                if direction == False:
                        ## they changed direction, rerun A*
                        rerun_astar = True
                        break
        
        if rerun_astar == True:
                ## ignore the rest of the loop and start over
                continue

        ## Start camera
        '''# ------ Insert Code here ----- #'''
        ## start camera and detect whether destination reached
        reached_destination = True
        '''# ------ End here ----- #'''

        if reached_destination == False:
                rerun_astar = True
        
        keepRunning += 1



                    

if __name__ == "__main__":
    tIds = pp.LoadData("Software/RouteFinding/Data/e5_4f.jpg")
    Nav_Thread(tIds)
