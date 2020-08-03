# Example_1

create_file = input("Type the file name: ")
name = input("Type your name: ")
age = int(input("Type your age: "))
city = input("Type your city: ")
file = open(create_file, "w")
file.write("Your name is "+name+". \n")
file.write(f"You are {0} years old. \n".format(str(age)))
file.write("You live in "+city+". \n")
file.close()
print("End of code")
