"""
A simple text-based adventure game called: Maze Trap

try and find the key and reach to the exit

you may need tools like a torch

Available commands include:
    go <compass direction>
    take <object>
    drop <object>
    inventory
    quit
"""

# current location: hallway, lounge or bedroom
state = "maze"

# the object that the player is carrying around (or "nothing").
carrying = []
###############################################################
# global dictionary of the movable objects in each location
items_in = {"maze" : [],
            "mazekey" : ["key"],
            "mazetorch"  : ["torch"],
            "mazechallenge"  : ["fake-key"],
            "mazedeadend"  : [],
            "mazeexit"  : []
            }

#####################################################
# Functions for describing the current location


def describe_maze():
    print("You have just entered into a maze, Good Luck!")
    print("Every room around you seems to be lit except the east room")
  
def describe_mazekey():
    if "torch" not in carrying:
        print("It's a dark room, might be something here.")
    else:
        print("Theres a key here, i didnt even realise. It was so dark")

def describe_mazetorch():
    if "torch" not in carrying:
        print("There's a torch on the table")
    else:
        print("You just took a torch, maybe it can be used somewhere")

def describe_mazechallenge():
    if "fake-key" not in carrying:
        print("Theres a key on the table")
    else:
        print("I might be able to keep going with this key")

def describe_mazechallenge1():
    print("there was nothing here after all")

def describe_mazedeadend():
    if "key" and "torch" in carrying:
        print("The torch reveals a secret key hole towrarads the north side")
    else:
        print("i dont think this room leads to anything?!?!")

def describe_mazeexit():
    print("You escaped, Thanks for playing!")
    
def describe():
    """Print a description of the current location."""
    if state == "maze":
        describe_maze()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 

    elif state == "mazekey":
        describe_mazekey()
        if "torch" in carrying:
            for item in items_in[state]:
                print("You can see: " + item + " maybe you can pick it up?.") 

    elif state == "mazetorch":
        describe_mazetorch()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 

    elif state == "mazechallenge":
        describe_mazechallenge()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 

    elif state == "mazechallenge1":
        describe_mazechallenge1()

    elif state == "mazedeadend":
        describe_mazedeadend()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 

    elif state == "mazeexit":
        describe_mazeexit()

    else:
        print("ERROR: unknown location: " + str(state))


#######################################################
# Functions for moving between locations

def move_maze(direction):
    if direction == "east":
        return "mazekey"
    elif direction == "north":
        return "mazedeadend"
    if direction == "south":
        return "mazetorch"
    elif direction == "west":
        return "mazechallenge"
    return ""

def move_mazekey(direction):
    if direction == "west":
        return "maze"
    return ""

def move_mazedeadend(direction):
    if direction == "south":
        return "maze"
    elif direction == "north" and "key" in carrying:
        return "mazeexit" 
    return ""

def move_mazetorch(direction):
    if direction == "north":
        return "maze"
    return ""

def move_mazechallenge(direction):
    if direction == "east":
        return "maze"
    elif direction == "west":
        return "mazechallenge1"
    return ""

def move_mazechallenge1(direction):
    if direction == "east":
        return "mazechallenge"
    return ""

def move_cmd(direction):
    """Attempt to move in the given direction.

    This updates the 'state' variable to the new location,
    or leaves it unchanged and prints a warning if the move was not valid.
    :param direction: a compass direction, "north", "east", "south", or "west".
    :return: None
    """
    global state
    if state == "maze":
        new_state = move_maze(direction)

    elif state == "mazetorch":
        new_state = move_mazetorch(direction)

    elif state == "mazechallenge":
        new_state = move_mazechallenge(direction)

    elif state == "mazechallenge1":
        new_state = move_mazechallenge1(direction)
        
    elif state == "mazedeadend":
        new_state = move_mazedeadend(direction)

    elif state == "mazekey":
        new_state = move_mazekey(direction)

    
    else:
        print("WARNING: move_cmd sees unknown state: " + state)
        new_state = ""
    # now check to see if it was a valid move
    if new_state == "":
        print("You cannot go " + str(direction) + " from here.")
    else:
        state = new_state


#########################################################
def take_cmd(obj):
    """Try to pick up the given object.
    Most objects can only be picked up when in the correct room.
    """
    global carrying
    #This looks for the object in the current room then picks it up and drops anything it is carrying
    if obj in items_in[state]: 
        carrying.append(obj)
        print("You picked up and carrying " + obj + ".")
        items_in[state].remove(obj)
    else:
        print("There is nothing to pickup!")

########################################################################

#this function is used to drop an object from your inventory to the current room
def drop_cmd(obj):
    if obj in carrying:
        items_in[state].append(obj)
        print("You dropped " + obj + ".")
        carrying.remove(obj)
    else:
        print("There is nothing to drop!")


#########################################################
def inventory_cmd():
    print("You are currently carrying:" + str(carrying))
########################################################################
# The main loop that processes the player's input commands.
def main():
    for turn in range(20, 0, -1):
        print("")
        describe()
        cmd = input("Enter your command " + str(turn) + "> ")
        cmd = str.lower(cmd) #This will turn any input command into lowercase   
        cmd_split = str.split(cmd) #This splits the input command into a list of words
        cmd = " ".join(cmd_split) #This turns the list of words into a single string
        

        if cmd == "quit":
            print("You gave in so easily :-(")
            break
        elif cmd.startswith("go "):
            where = cmd[3:]
            move_cmd(where)
            if state == "outside":
                print("You push the door open with the heavy aquarium and escape to outside!")
                break
        elif cmd.startswith("take "):
            obj_name = cmd[5:]
            take_cmd(obj_name)
        elif cmd.startswith("drop "):
            obj_name = cmd[5:]
            drop_cmd(obj_name)
        elif cmd == "inventory":
            inventory_cmd()
        else:
            print("I do not understand '" + cmd + "'.  Try go/take/drop/inventory/quit")
    print("Game over")


if __name__ == "__main__":
    main()
