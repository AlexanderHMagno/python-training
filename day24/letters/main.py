import os

# Read friends
with open("friends.txt", "r") as file:
    friends = file.readlines()

# Read letter
letter = ""
with open("./layout.txt", "r") as file:
    letter = file.read()

# Create output folder
os.makedirs("./output_letters")

# Write letters
for friend in friends:
    with open(f"./output_letters/letter_for_{friend}.txt", "w") as file:
        file.write(letter.replace("[name]", friend.strip()))
