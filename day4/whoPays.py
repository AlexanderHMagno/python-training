import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]


#option 1
# print(f"{random.choice(names)} is going to buy the meal today!")

#option 2
random_integer = random.randint(0,len(names)-1)
print(f"{names[random_integer]} is going to buy the meal today!")
