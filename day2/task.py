print("Welcome To The Tip Calculator")

total_bill = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? ")
number_of_people = input("How many people to split the bill? ")

print(type(total_bill))
print(type(tip_percentage))
print(type(number_of_people))

tip_percentage = float(tip_percentage)
total_bill = float(total_bill)
number_of_people = int(number_of_people)

tip_amount = total_bill * tip_percentage / 100
total_amount = total_bill + tip_amount
amount_per_person = total_amount / number_of_people

print(f"Each person should pay: ${amount_per_person:.2f}")

