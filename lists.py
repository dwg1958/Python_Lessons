print("LISTS")
print()

dognames = ["Harley", "Fido", "Tiddles", "Butch"] #always keep same order
print(f"{dognames} - raw list (array)")

dognames.insert(2, "Jojo")
print(f"{dognames} - added one name at position 2")

print(f"NB- dognames[2] = {dognames[2]}")

del(dognames[1])

print(f"{dognames} - deleted position 1")
print(f"NB- dognames[2] = {dognames[2]}")

print(f"Number of entries: {len(dognames)} - being:")
for name in dognames:
    print("  "+name)

# TUPLES - https://www.w3schools.com/python/python_tuples.asp
print ("")
print("TUPLES - unchangeable")
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])  # start at position 2 (third) and go to  - but not including - position 5
