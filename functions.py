print('FUNCTIONS')
print('')

a = 3
b = 5
quote = ("What is being divided is called the dividend, which is divided by \n"
         "the divisor, and the result is called the quotient, i.e.")

# Functions
def sumnum(x, y):
    print(f"Numbers = {x} and {y}")
    print("Numbers = {} and {}".format(x, y))
    print(f"Sum = {x + y} and", end=" ")
    print(f"multiple = {x * y}")
    return x / y

tt = sumnum(a, b)

print('')
print(f"{quote} {tt}")

# TODO this is a todo
