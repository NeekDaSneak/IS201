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

"""
from collections import Counter

# Input list
input_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# Count frequencies of each element
element_counts = Counter(input_list)

# Extract elements with count > 1
output_list = [item for item, count in element_counts.items() if count > 1]

print("Output list:", output_list)
"""

"""
# Define the initial menu as a tuple
menu = ("Grilled Chicken", "Mashed Potatoes", "Cornbread", "Green Beans", "Mac and Cheese")

# Print the original menu
print("Original Menu:")
for food in menu:
    print(f"- {food}")

# Attempt to modify one of the items (this should raise a TypeError)
try:
    menu[0] = "Fried Chicken"
except TypeError as e:
    print("\nError: Cannot modify a tuple item. Tuples are immutable.")
    print("Exception message:", e)

# The restaurant changes the menu – replacing two items
menu = ("Fried Chicken", "Mashed Potatoes", "Cornbread", "Teriyaki", "Baked Beans")

# Print the updated menu
print("\nUpdated Menu:")
for food in menu:
    print(f"- {food}")
"""

"""
# Input list of tuples
input = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

# Sort by the second item in each tuple
output = sorted(input, key=lambda x: x[1])

# Output the sorted list
print(output)
"""