# Doing Things to List

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it.")

# splitting the variable stuff when it finds ' ' (space) and make it a list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana",
                "Girls", "Boy"]


while len(stuff) != 10:
    # Take one item on list more_stuff from the first index
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    # adding it to list stuff
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print("There we go:", stuff)

print("Let's do some things with stuff.")

# print the 2nd item/index x item in list stuff
print(stuff[1])
# print the the first item from the last in list stuff
print(stuff[-1]) # Whoa Fancy
# popping the 1st item/ index 0 from list stuff
print(stuff.pop())
# joining every items in stuff list and add ' '(space) between them
print(' '.join(stuff))
# joining the 3rd index and 4th index from stuff list and add '#' between them
print('#'.join(stuff[3:5]))
