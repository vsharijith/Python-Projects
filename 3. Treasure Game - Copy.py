print("Welcome to Treasure Island.\nYour Mission is to find the treasure.\nInorder to proceed choose the correct path")

activity1 = input("Which direction do you want to go? Type 'right' or 'left'\n")
if activity1 == "left":
    print("Congrats you have chosen the right path. Proceed further")
else:
    print("GAME OVER! You fell into a Hole")
    exit()

print("Ooops! There is a lake in front of you.")
activity2 = input("Type what you want to do, 'swim' or 'wait'\n")
if activity2 == "wait":
    print("Well done! You are succeeding. Keep going.")
else:
    print("GAME OVER! You have been attacked by a Trout")
    exit()

print("Look carefully, an island is poping from the lake and now you have 3 doors in fleront of you")
activity3 = input("Type the correct door to the room where the treasure is\nYou have 3 options - 'Red', 'Blue', and 'Yellow'\n")
if activity3 == "yellow":
    print("YOU WIN!")
elif activity3 == "red":
    print("GAME OVER! You are burnt in fire")
    exit()
elif activity3 == "blue":
    print("GAME OVER! YOu are eaten by a beast")
    exit()
else:
    print("GAME OVER!")
    exit()
