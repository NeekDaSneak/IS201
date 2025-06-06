'''
# Initial guest list
guests = ["Alice", "Bob", "Charlie"]
print("Initial guest list:", guests)

# Replace a guest who can't make it
guests[1] = "David"
print("Updated guest list:", guests)

# Add new guests
guests.insert(0, "Eve") # Beginning
guests.insert(2, "Frank") # Middle
guests.append("Grace") # End

print("Expanded guest list:", guests)

# Remove guests until only 2 remain
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, you can't come to dinner.")

print("Final guest list:", guests)
'''
"""
animals =["Lion", "Bear", "Shark", "Elephant", "Giraffe", "Horse", "Chettah"]

print("The first three items on the list are:") # This part of the code loops through the first three animals on the list then prints them.
for animal in animals[:3]:
    print(animal.title())

print("The three items from the middle of the list are:") # This part of the code loops through the next three animals on the list then prints them.
for animal in animals[2:5]:
    print(animal.title())

print("The last three item in the list are:") # This part of the code loops through the last three animals on the list then prints them.
for animal in animals[4:7]:
    print(animal.title())
"""

