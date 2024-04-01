print("Welcome to Treasure Island.\nYour mission is to find the treasure")
direction = input("you arrive at a cross roads type 'left' or 'right'!\n").lower

if direction == "left":
    wait = input("you continue walking until you hit a lake and can type 'swim' to swim or 'wait'to wait for a boat\n").lower
    if wait == "wait":
        door = input("You arrive at three sets of doors tyep 'red', 'blue' or 'yellow' to choose\n").lower
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire\nGame Over")
        else:
            print("Attacked by Beasts \nGame over")
    else:
        print("You are killed by alligators\nGame Over")

else:
    print("Fall into a hole \n Game Over.")