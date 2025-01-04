#what is a dictionary?
#a dictionary is a collection of key-value pairs
#the keys are unique and the values are not
#the keys are immutable and the values are mutable

#example of a dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

#how to access the value of a key
print(student_scores["Harry"])

#how to add a new key-value pair
student_scores["Snape"] = 65

#how to update the value of a key
student_scores["Hermione"] = 99

#how to remove a key-value pair
del student_scores["Draco"]

#how to iterate through a dictionary
for key in student_scores:
  print(key)

#how to get the keys of a dictionary
print(student_scores.keys())

#how to get the values of a dictionary
print(student_scores.values())

#how to get the items of a dictionary
print(student_scores.items()) 