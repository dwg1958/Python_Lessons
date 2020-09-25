#############################
print("PYTHON")
## - https://www.w3schools.com/python/default.asp

################################################################
################ LOCAL DATA STORAGE ############################
################################################################

## DICTIONARY ###############
dogs_dictionary = {"Harley": 5, "Fido": 9, "Tiddles": 2, "Fang": 12}
# NB No order
# Add and delete
del (dogs_dictionary["Tiddles"])
dogs_dictionary["Woofer"] = 5.5
# Change value
dogs_dictionary["Harley"] = 6

## LIST #####################
dogs_list       = ["Harley", "Fido", "Tiddles", "Butch"]
#always keep same order
del(dogs_list[1])
dogs_list.insert(2, "Jojo")

## TUPLE ####################
fruit_tuple     = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# TUPLES - https://www.w3schools.com/python/python_tuples.asp
# Unchangeable once set up
print(fruit_tuple[2:5])  # start at position 2 (third) and go to  - but not including - position 5
# so that this works:
print(fruit_tuple[2:len(fruit_tuple)])

############################################################
# Turn list into dictionary ################################
############################################################

doggie_dict = {}
age = 1
for dog in dogs_list:
    doggie_dict[dog] = age
    age += 1
print(doggie_dict)

############################################################
# Turn dictionary into a list of tuples ####################
# https://www.w3schools.com/python/ref_dictionary_items.asp
dog_ages = dogs_dictionary.items()
print(dog_ages)
## ([('Harley', 6), ('Fido', 9), ('Fang', 12), ('Woofer', 5.5)])
# Print them:
for dog, age in dog_ages:
  print(f"{dog} = {age}")

# BUT - beware that the list object items change if you change the source dictionary !!!!!!!!!
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
view_object = car.items()
print(view_object)
car["year"] = 2018
print(view_object)
