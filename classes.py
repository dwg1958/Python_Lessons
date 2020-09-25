print("CLASSES")


# create basic class
class Dog:
    dogInfo = "Put dog info here"

    def bark(self, string):  # a function in a class is called a Method
        print("Bark " + string + " !")


# create an instance of the class
mydog = Dog()
mydog.bark("this is the argument str")

# Now add parameters to class
mydog.name = "Harley"
mydog.age = 5

print(f"{mydog.name} is {mydog.age} years old")

# replace current values
mydog.dogInfo = "He's a good boy"

print(mydog.dogInfo)


# ARGUMENTS AND DEFAULTS #################################
class Bike:
    def __init__(self, year="", color="TBA", cc=0):
        self.year = year
        self.color = color
        self.capacity = cc

    def profile(self):
        print(f"My bike is {self.color}, size {self.capacity}cc and was made in {self.year}")



harley = Bike()  # takes default values
print(harley.capacity)
print(harley.profile())

hd = Bike("2017", "red", 1850)
print(hd.profile())
