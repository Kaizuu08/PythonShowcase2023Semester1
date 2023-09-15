"""
A simple text-based adventure game called: Creepy House.

Available commands include:
    go <compass direction>
    take <object>
    quit
"""

# current location: hallway, lounge or bedroom
state = "hallway"

# the object that the player is carrying around (or "nothing").
carrying = []
###############################################################
# global dictionary of the movable objects in each location
items_in = {"bedroom" : ["aquarium", "bats"],
            "hallway" : [],
            "lounge"  : ["stereo"]
            }

#####################################################
# Functions for describing the current location


def describe_bedroom():
    print("You are in a bedroom.")
    print("There is a bit of furniture in here, looks like pet fish... or what use to be.")
    print("It seems they like cricket too?")
  

def describe_hallway():
    print("You are in a dark hallway.")
    print("There are painting on the wall of what seems to be a family.")
    print("There is also a bright light to the west")

def describe_lounge():
    print("You are in a brightly-lit lounge, with two red sofas and something is playing.")
    
def describe():
    """Print a description of the current location."""
    if state == "hallway":
        describe_hallway()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 
    elif state == "lounge":
        describe_lounge()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 
    elif state == "bedroom":
        describe_bedroom()
        for item in items_in[state]:
            print("You can see: " + item + " maybe you can pick it up?.") 
    else:
        print("ERROR: unknown location: " + str(state))


#######################################################
# Functions for moving between locations

def move_lounge(direction):
    if direction == "west":
        return "bedroom"
    elif direction == "east":
        return "hallway"
    return ""


def move_hallway(direction):
    if direction == "west":
        return "lounge"
    elif direction == "east" and carrying == "aquarium":
        return "outside"
    return ""


def move_bedroom(direction):
    if direction == "east":
        return "lounge"
    return ""


def move_cmd(direction):
    """Attempt to move in the given direction.

    This updates the 'state' variable to the new location,
    or leaves it unchanged and prints a warning if the move was not valid.
    :param direction: a compass direction, "north", "east", "south", or "west".
    :return: None
    """
    global state
    if state == "hallway":
        new_state = move_hallway(direction)
    elif state == "lounge":
        new_state = move_lounge(direction)
    elif state == "bedroom":
        new_state = move_bedroom(direction)
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
