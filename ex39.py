# Dictionaries, Oh lovely Dictinaries

# Create a mapping of state to abbreviation

states = {
    'Oregon': "OR",
    'Florida': "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# Create a basi set of states and some cities in them

cities ={
    "CA": "San Fransisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print("-"*10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print("-"*10)
print("Michigan's abrreviation is: ", states["Michigan"])
print("Florida's abrreviation is: ", states["Florida"])

# do it by using the state then the cities dict
print("-"*10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abrreviation
print("-"*10)
for state, abrrev in list(states.items()):
    print(f"{state} is abrreviated {abrrev}")

# print every city in state
print("-"*10)
for abrrev, city in list(cities.items()):
    print(f"{abrrev} has the city {city}")

# Now do both at the same time
print("-"*10)
for state, abrrev in list(states.items()):
    print(f"{state} state is abrreviated {abrrev}")
    print(f"and has a city {cities[abrrev]}")

print("-"*10)
# Savely get a abrreviated by states that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas")

# get a city with a default value
city = cities.get("TX","Does not exist")
print(f"The city for the state 'TX' is: {city} ")

print("Asping lives in %s" % states.get("asping", "Nowhere"))
