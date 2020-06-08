# Loops and Lists

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# First type of for-loop on a list
for i in the_count:
    print(f"This is count {i}")

for f in fruits:
    print(f"fruit of type: {f}")

# Also we can through mixed lists too
# notice we have to use {} since we dont know what's in it
for c in change:
    print(f"I got {i}")

# We can also build lists, first start with an empty list
element = []

# Then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # Append is a function that lists understand
    element.append(i)

# Now we can print them out too
for i in element:
    print(f"Element was: {i}")
