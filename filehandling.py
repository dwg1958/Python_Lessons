

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""


try:
    f = open("myfile.txt", "x") # Create
except:
    print("File already exists, but carry on anyway")
finally:
    f = open("myfile.txt", "w") # Open if we couldn't create
# ( or could just have used f = open("myfile.txt", "a") )

f.write("Woops! I have deleted the content again!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())
