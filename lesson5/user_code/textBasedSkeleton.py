import time


def save(start_place):
    save1.write(start_place + '\n' + str(inventory))
    print("Game saved")


def win():
    print("You win!?!")
    print("Aren't you happy!")
    quit()


def engineering_bay():
    print("You enter into the engineering bay")


def escape_shuttle():
    print("")


def corridor():
    print("You enter into a dark corridor, the only light from a cracked fluorescent tube running above your head")
    input()
    print("The corridor stretches into the dark either side of you")
    input()
    player_choice = ask_player('(1) Go left (2) Go right (3) Save', 3)
    if player_choice == 1:
        engineering_bay()
    elif player_choice == 2:
        escape_shuttle()
    else:
        save("corridor")
        corridor()


def try_door():
    print("The door is locked")
    input()
    if 'keyCard' in inventory:
        player_choice = ask_player("(1) Use key (2) Return (3) Save", 3)
        if player_choice == 1:
            corridor()
        elif player_choice == 2:
            start_game()
        else:
            save("try_door")
            try_door()
    else:
        start_game()


def look_around_1():
    print("You look around and see several janitor uniforms as well as assorted cleaning products")
    input()
    print("On inspection, you find a key card in one of the uniforms")
    input()
    print("It seems a janitor forgot it")
    input()
    print("You place it in your inventory")
    input()
    inventory.append('keyCard')
    start_game()


def ask_player(options, num_options):
    player_choice = []
    options1 = list(range(0, num_options))
    for x in range(1, num_options + 1):
        options1[x-1] = x

    while player_choice not in options1:
        print("What do you want to do?")
        print(options)
        player_choice = int(input())
    return player_choice


def start_game():
    print("In front of you there is the door")
    input()
    player_choice = ask_player("(1) Examine the door (2) Look around (3) Save", 3)
    if player_choice == 1:
        try_door()
    elif player_choice == 2:
        look_around_1()
    else:
        save("start_game")
        start_game()


def preamble():
    print("You awaken in a cramped storage room")
    input()
    print("Above you an emergency light frantically blinks and sirens blare")
    input()
    start_game()


def start():
    print("Welcome to ...")
    print("Choices are presented with a number in curved brackets to the left")
    print("Enter this corresponding number to select that action")
    print("Press enter to move text along")
    print("Press enter to begin")
    input()
#    if
#        ...
#    else:
#        ...
    preamble()


inventory = []
save1 = open('save.txt', 'w+')
myFile = open('textBasedSkeleton.txt', 'a')
myFile.write('\n' + time.strftime('%d:%b:%Y') + ' ' + time.strftime('%H:%M'))
myFile.close()
start()
