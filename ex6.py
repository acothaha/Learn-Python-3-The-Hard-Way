#Exercise 6. Strings and Text

# making some variables consist of integer and string
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# printing variables individually
print(x)
print(y)

# printing the variable x and y with some string attach to it
print(f"I said: {x}")
print(f"I also said: {y}")

# a variable that will be called by another variable using .format
hilarious = False

# a variable that will be calling another variable using .format later
joke_evaluation = "Isn't that joke so funny?! {}"

# printing a variable using .format to attach another variable to its content (string)
print(joke_evaluation.format(hilarious))

# make some variables
w = "This is the left side of..."
e = "a string with a right side"

# printing the addition of two variable using a math symbol (+)
print(w + e)
