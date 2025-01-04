import random
import ascci


number_of_lives = 6
game_over = False

def print_placeholder(placeholder):
    print(" ".join(placeholder))

def print_hangman(number_of_lives):
    print(ascci.hangman_stages[number_of_lives])


chosen_word = random.choice(ascci.word_list)

#generate placeholder
placeholder = []
for letter in chosen_word:
    placeholder.append("_")

print_placeholder(placeholder)
#list of guessed letters
guess_letter = []

#loop through the game
while not game_over:
    
    guess = input("Guess a letter: ").lower()
    #check if the guess is already in the list of guessed letters
    if guess in guess_letter:
        print("You already guessed that letter!")
        continue
    
    #add the guess to the list of guessed letters
    guess_letter.append(guess)

    print(guess_letter)
    
    #check if the guess is in the chosen word
    if guess not in chosen_word:
        number_of_lives -= 1
    else:
        #check if the guess is in the chosen word
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                placeholder[index] = guess
      
    print_placeholder(placeholder)
    print_hangman(number_of_lives)
    
    #check if the placeholder has no underscores
    if "_" not in placeholder:
        print("#######################You win!#######################")
        game_over = True
        break

    if number_of_lives == 0:
        print("#######################You lose!#######################")
        game_over = True
        break

  