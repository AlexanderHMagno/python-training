
import random

def rockpaperscissors(choose):
    choose = int(choose)
    if choose == 0:
        print("Rock")
    elif choose == 1:
        print("Paper")
    else:
        print("Scissors")



choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))


print("You chose:")
print(rockpaperscissors(choose))

computer_choose = random.randint(0, 2)
print("Computer chose:")
print(rockpaperscissors(computer_choose))



if choose == computer_choose:
    print("It's a draw!")
elif choose == 0:
    if computer_choose == 2:
          print("You win!")
    else:
        print("You lose!")
elif choose == 2:
    if computer_choose == 0:
        print("You lose!")
    else:
        print("You win!")
elif choose == 1:
    if computer_choose == 0:
        print("You win!")
    else:
        print("You lose!")



