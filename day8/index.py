#set alphabet
alphabet = [chr(i) for i in range(97, 123)]
terminate = False

#cesar cypher 

def cesar_cypher(text, shift, direction):

  #new text to return
  new_text = ""

  #if direction is decypher, shift is negative
  if direction == "d":
    shift = -shift     

  #loop through each letter in the text
  for letter in text:
    index = alphabet.index(letter)
    if index != -1:
      new_letter = (index + shift) % len(alphabet)
      new_text += alphabet[new_letter]
    else:
      new_text += letter

  return new_text




while not terminate:    

  #Get direction to cypher or decypher from user
  direction = input("Do you want to cypher or decypher? (c/d): ")

  #Get text to cypher or decypher from user
  text = input("Enter the text to cypher or decypher: ")

  #Get shift to cypher or decypher from user
  shift = int(input("Enter the shift: "))

  #print the new text
  print(cesar_cypher(text, shift, direction))

  #if user wants to terminate, set terminate to True
  if input("Do you want to terminate? (y/n): ").lower() == "y":
    terminate = True  

