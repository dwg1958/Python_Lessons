print("LOOPS")
print('')

top = 16

# FOR LOOPS
print("---SIMPLE FOR---")

for i in range(top + 1):  # count from zero
    print(i, end=", ")

print("")
print("---COMPLEX FOR---")

for i in range(0, top + 1):  # count from zero
    if i < top:
        print(i, end=", ")
    else:
        print(f'{i}')  # No 'end=' so we get <CR>

print("---WHILE---")

# WHILE LOOPS
while top > 1:
    print(top, end=", ")
    top -= 1

# Loop doesn't print 1 because while condition is false, so..
print("and " + str(top))
