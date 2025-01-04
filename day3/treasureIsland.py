print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

action = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.")

if action == "left":
    action = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if action == "swim":
        print("You swam across and were eaten by an angry trout. Game Over.")
        exit()
    elif action == "wait":
        print("You waited for a boat. The boat arrived and you crossed the lake. You're on the island.")
else:le
    print("You fell into a hole. Game Over.")
    exit()




action = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?")

if action == "red":
    print("It's a room full of fire. Game Over.")
    exit()
elif action == "yellow":
    print("You enter a room of beasts.But.")
elif action == "blue":
    print("You enter a room of beasts. Game Over.")
    exit()
else:
    print("You chose a door that doesn't exist. Game Over.")
    exit()
print("You found the treasure! You Win!")
