import subprocess 

def GenerateWalkCommand(command):
    if command[0] == 0:
        return "Move forward " + str(command[1]) + " steps"
    elif command[0] == 2:
        return "Turn right and take " + str(command[1]) + " steps"
    elif command[0] == 1:
        return "Turn left and take " + str(command[1]) + " steps"

def SpeakCommand(command):
    subprocess.call(["espeak", command, "2>/dev/null"])