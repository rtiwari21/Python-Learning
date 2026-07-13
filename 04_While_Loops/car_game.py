# Car Game

command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Already started...")
        else:
            started = True
            print(" Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped...")
    elif command == "help":
        print("start\nstop\nquit")
    elif command == "quit":
        break
    else:
        print("I don't understand the command")