#guess the number
from random import randint
from ascii import guess_the_number_logo, lives_icon

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

play_again = True

def print_lives(lives):
  print((lives_icon + " ") * lives)

def define_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")  
  return HARD_LEVEL_TURNS if difficulty == "hard" else EASY_LEVEL_TURNS


#game logic
while play_again:
  #print logo
  print(guess_the_number_logo)

  #choose a number between 1 and 100
  number = randint(1, 100)

  #lives
  lives = define_difficulty()

  #check if the guess is correct
  while lives > 0:
    print_lives(lives)
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
      print("You won!")
      break
    elif guess < number:
      print("Too low.")
    elif guess > number:
      print("Too high.")
    lives -= 1

    if lives == 0:
      print("You lost!")
  
  #play again
  play_again = input("Do you want to play again? Type 'y' or 'n': ")
  if play_again == "n":
    play_again = False
    print("Goodbye!")

