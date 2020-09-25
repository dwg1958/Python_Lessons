print("DICTIONARIES")
print('')

dogs = {"Harley": 5, "Fido": 9, "Tiddles": 2, "Fang": 12}  # NB No order

print(dogs)

print(f" Harley's age is {dogs['Harley']}")  # use different quotes!

# Change value
mydog = "Harley"
dogs[mydog] = 6

print(f" Harley's age is {dogs['Harley']}")  # use different quotes!

# Add and delete
del (dogs["Tiddles"])
dogs["Woofer"] = 5.5

print(dogs)

