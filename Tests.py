from Software.RouteFinding.PictureProcessing import pp_module as pp
from Software.RouteFinding.PictureProcessing import opencv_wrapper as wo_cv2
# from Software.RouteFinding.PictureProcessing import matplot_wrapper as wo_plt
from Software.RouteFinding.PathFinding import pf_module as pf
from Software.RouteFinding.Data import symposium_map as d
import numpy as np
import matplotlib.pyplot as plt

def DebugPathFinding():
    # img_label, _ = pp.ReadImage("Software/RouteFinding/Data/symposium_map.jpg")
    img, edged = pp.ReadImage("Software/RouteFinding/Data/symposium_map.jpg")
    tVertInd = pp.CreateNavMesh(edged)
    tIds = pp.GetTriangles(tVertInd)

    ## Get user input 
    s = input("Enter starting room: ")
    e = input("Enter destination room: ")

    start = d.rooms[s][0] ## returns a list, take first value
    end = d.rooms[e][0]

    ## Run A* 
    coordinates, path, _ = pf.FindPath(tIds, start, end)
    instructions = pf.GetInstructions(coordinates, d.mapScale*d.strideMen)

    print(instructions)
    print(coordinates)

    imgLines = wo_cv2.DrawLines(coordinates, img.copy(), 3)
    imgFinal = wo_cv2.DrawCircles((start, end), imgLines, 3)
    wo_cv2.DisplayImage('Final image', imgFinal)    
    # wo_plt.DrawTriangles(tIds, path, 'hide')
    # wo_plt.ScatterPoints(coordinates, 'yellow')
    # wo_plt.ShowPlot()

DebugPathFinding()