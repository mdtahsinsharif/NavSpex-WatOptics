import subprocess 

VOICE_STEPS_THRESHOLD = 5

def GenerateWalkCommand(command):
    cmd = ""

    if command[0] == 0:
        cmd += "Walk forward "
    elif command[0] == 2:
        cmd += "Turn right and walk forward "
    elif command[0] == 1:
        cmd += "Turn left and walk forward "

    if command[1] <= VOICE_STEPS_THRESHOLD:
        cmd += str(command[1])
        if command[1] == 1:
            cmd += "step"
        else:
            cmd += "steps"
    else:
        cmd += "till next instruction."
    
    return cmd


def SpeakCommand(command):
    subprocess.call(["espeak", command, "2>/dev/null"])