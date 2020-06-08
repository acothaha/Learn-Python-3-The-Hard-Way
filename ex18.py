# Names, Variables, Code, Function

# This one is like your scripts with argv
def print_two(*args):
    print(args)

# Instead of doing that, you can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no aargument
def print_none():
    print("I got nothing")

print_two("Asping","Palawehweh","123","123423")
print_two_again("Asping","Palawehweh")
print_one("First!")
print_none()
