

with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)



with open("myfile.txt", "a") as file:
    file.write("Hello, World!\n")
