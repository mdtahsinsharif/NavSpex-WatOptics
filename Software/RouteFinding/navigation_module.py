from PictureProcessing import pp_module as pp
from PictureProcessing import opencv_wrapper as wcv2
from PathFinding import pf_module as pf
from UserInterfacing import ui_module as ui
from Data import e5_4f as d ## TODO: Figure out how to change this based on user input

def Load_Data(path):
    img, edged = pp.ReadImage(path)
    tVertInd = pp.CreateNavMesh(edged)
    tIds = pp.GetTriangles(tVertInd)
    return tIds

def Nav_Thread(tIds):
    ## Get current location
    s = "4020"

    ## Get destination
    e = "4117"

    ## Map start and end to coordinates:
    start = d.rooms[s][0] ## returns a list, take first value
    end = d.rooms[e][0]

    # while(True):
    ## Run A* 
    coordinates, _, _ = pf.FindPath(tIds, start, end)
    instructions = pf.GetInstructions(coordinates, d.mapScale*d.strideMen)

    for inst in range(len(instructions)):
        ## send instruction
        command = ui.GenerateWalkCommand(inst)
        subprocess.call(["espeak", command])
                    

if __name__ == "__main__":
    tIds = Load_Data("Data/e5_4f_nolabel.jpg")
    Nav_Thread(tIds)
