# While Loops

i = 0
a = 9
numbers = []

while i < a:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 3
    print(f"Numbers now: {numbers}")
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
