from sys import exit

## Below is a skeleton to a text based video game
def first_room():
    print("There is a door straight infront of you.")
    print("To your left is a cabinet with the face of legendary wrestler, Nacho Libre, embossed on it.")
    print("To your right is a small packet of nachos.")
    print("")
    print("You can:")
    print("(1) Enter the door.")
    print("(2) Eat the nachos.")
    print("(3) Examine the cabinet.")
    print("")
    user_input = ""
    while(user_input != "1" and user_input != "2" and user_input != "3"):
        print("What do you do? (Please enter 1, 2 or 3)")
        user_input = input()

    if(user_input == "1"):
        enter_door()
    elif(user_input == "2"):
        die("eaten", "packet of nachos")
    else:
        examine_cabinet()

def enter_door():
    print("On closer inspection, you realise the door is closed.")
    print("You go back to where you were before.")
    first_room()

def examine_cabinet():
    print("You notice in the face of Nacho Libre, embossed onto the cabinet, there is a small, nacho size, space.")
    print("What do you want to do?")
    ##It's up to you what to put! It's your game!

def start():
    print("You awake in a strange, dark room.")
    first_room()



def die(verb, noun):
    print("Oh dear, you have died!")
    print("Turns out you shouldn't have " + verb + " that " + noun + "!")
    print("Better luck next time!")
    exit(0)


start()