def GenerateWalkCommand(command):
    if command[0] == 'F':
        return "Move forward " + command[1] + " steps"
    elif command[0] == 'R':
        return "Turn right and take " + command[1] + " steps"
    elif command[0] == "L":
        return "Turn left and take " + command[1] + " steps"