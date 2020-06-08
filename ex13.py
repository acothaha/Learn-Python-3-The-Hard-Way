# Parameters, Unpacking and Variables

from sys import argv
# read the WYSS section on how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

person1 = input(f"Pick a person to be attached to the {first} variable: ")
person2 = input(f"Pick a person to be attached to the {second} variable: ")
person3 = input(f"Pick a person to be attached to the {third} variable: ")
