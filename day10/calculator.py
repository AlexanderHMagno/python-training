
#calculator program

#set a variable to continue the program
continue_program = True
result = ""

#create a function to do the math based on the operation
def do_math(num1, num2, operation):
  '''
  Do the math based on the operation
  Args:
    num1 (str): The first number
    num2 (str): The second number
    operation (str): The operation to perform
  Returns:
    float: The result of the operation
  '''
  #convert num1 and num2 to float
  num1 = float(num1)
  num2 = float(num2)

  #transfrom into a dictionary
  operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2
  }
  #do the math
  return operations[operation]


def request_operation():
  '''
  Request the operation from the user
  Returns:
    str: The operation
  '''

  #print the operation options
  print("+")
  print("-")
  print("*")
  print("/")  

  return input("What is the operation? ")


while continue_program:
  
  #Pick number

  result = result if result != "" else input("What is the first number? ")  

  #Pick operation
  operation = request_operation()

  #Pick number
  user_input = input("What is the second number? ")

  #Do math
  result = do_math(result, user_input, operation)

  #Show result
  print(f"The result is {result}")

  #Check if user wants to continue calculating with the result
  if input("Do you want to continue calculating with the result? (y/n): ").lower() == "n":
      result = ""
#Show result