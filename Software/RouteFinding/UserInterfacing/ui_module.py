import subprocess 

VOICE_STEPS_THRESHOLD = 5

'''
0 - forward
1 - left
2 - right
'''

def GenerateTurnCommand(command):
    cmd = "Turn "
    if command[0] == 1:
        cmd += "left "
    else:
        cmd += "right "
    
    cmd += "and press the done button to confirm."
    return cmd
        


def GenerateWalkCommand(command):
    cmd = "Walk forward "
    if command[1] <= VOICE_STEPS_THRESHOLD:
        cmd += str(command[1])
        if command[1] == 1:
            cmd += " step"
        else:
            cmd += " steps"
    else:
        cmd += " till next instruction."
    
    return cmd


def SpeakCommand(command, debug = 0):
    if debug:
        print(command)
    else:
        subprocess.call(["espeak", command, "2>/dev/null"])