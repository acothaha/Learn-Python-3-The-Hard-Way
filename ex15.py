# Reading Files

# importing a funtion argv from sys module
from sys import argv

# unpacking argv into 2 variables
script, filename = argv

# opening the file according to the filename variable that was inputed
# in command line, and assign it to variable txt
txt = open(filename)

# printing the filename variable that  was inputed earlier
print(f"Here's your file {filename}:")
# printing the reading of content in the file
# which was assigned to variable txt
print(txt.read())

# printing a string to inform the user to input the filename again
print("Type the filename again:")
# inputing the filename again
file_again = input(">")

# as the same as the variable txt, but using variable file_again
txt_again = open(file_again)

# same as earlier, but with variable txt_again
print(txt_again.read())
