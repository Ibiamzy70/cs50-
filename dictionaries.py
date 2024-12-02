houses = {"harry": "gryffindor", "draco": "slytherin"}

# Ask the user for a name
name = input("Enter a name: ").lower()

# Check if the name exists in the dictionary and print the house
if name in houses:
    print(f"{name.capitalize()} belongs to {houses[name].capitalize()}.")
else:
    print(f"Sorry, {name.capitalize()} is not in the list.")

