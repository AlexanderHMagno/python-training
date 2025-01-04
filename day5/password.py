import random

letters_source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_source = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_source = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")

print("How many letters would you like in your password?")
letters = int(input())

print("How many symbols would you like?")
symbols = int(input())

print("How many numbers would you like?")
numbers = int(input())

password_list = []

for char in range(0, letters):
    password_list.append(random.choice(letters_source))

for symbol in range(0, symbols):
    password_list.append(random.choice(symbols_source))

for number in range(0, numbers):
    password_list.append(random.choice(numbers_source))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)