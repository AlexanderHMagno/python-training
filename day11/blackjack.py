import random
from ascii import blackjack_logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True
#get two cards for each player  

table = {
  "user_cards": [],
  "computer_cards": []
}

def print_cards(full_computer_cards = False):
  print(f"Your cards: {table['user_cards']}, current score: {sum(table['user_cards'])}")
  if full_computer_cards:
    print(f"Computer's cards: {table['computer_cards']} , current score: {sum(table['computer_cards'])}")
  else: 
    print(f"Computer's cards: {table['computer_cards'][0]}")

#build a blackjack game with a function to deal cards
def deal_card():
  return random.choice(cards)

def shuffle_cards():
  for _ in range(2):
    table['user_cards'].append(deal_card())
    table['computer_cards'].append(deal_card())


def reset_table():
  for key in table:
    table[key] = []

def start_game():
  print(blackjack_logo)
  reset_table()
  shuffle_cards()
  print_cards()

#compare scores
def compare_scores():
  print_cards(True)
  if sum(table['user_cards']) > 21:
    print("You went over. You lose.")
  elif sum(table['computer_cards']) > 21:
    print("Computer went over. You win.")
  elif sum(table['user_cards']) > sum(table['computer_cards']):
    print("You win.")
  else:
    print("You lose.")

while play_again:
    start_game()
  
    #would you like to draw another card?   
    while True:
        another_card = input("Do you want to draw another card? (y/n): ") 
        if another_card == "y":
          table['user_cards'].append(deal_card())
          print(f"Your cards: {table['user_cards']}, current score: {sum(table['user_cards'])}")
        else:
          break


    #compare scores
    compare_scores()

    #play again or not
    if input("Do you want to play again? (y/n): ") == "n":
      play_again = False