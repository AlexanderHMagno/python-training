from data import data
from logos import logo, vs_logo
import random

OPTIONS = ["A", "B"]
game_over = False



def compare_followers(person1, person2):
  return (OPTIONS[0] if person1['followers'] > person2['followers'] else OPTIONS[1]).lower()

def select_two_entries():
  person1 = random.choice(data)
  person2 = random.choice(data)
  while person1 == person2:
    person2 = random.choice(data)
  return person1, person2

def print_entries(person1, person2):
  print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
  print(vs_logo)
  print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")


print(logo)



#game logic

#add a counter for the number of guesses
counter = 0 

while True:
  #select 2 random entries from the data list
  person1, person2 = select_two_entries()
  
  #display famous people
  print_entries(person1, person2)

  #ask the user to guess who has more followers
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()


  #if the user guesses correctly, print "You're right!"
  if guess == compare_followers(person1, person2):
      print("You're right!")
      counter += 1
      print(f"You've guessed {counter} times")
      print(f"{person1['name']} has {person1['followers']} followers", f"{person2['name']} has {person2['followers']} followers")
  else:
      print("You're wrong!, Game over!")
      break



