# --------------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Use case for pickling and structured error handling. This program
#              allows a user to create a list of characters and their general
#              affinity for them. The file is stored as a generic data file with
#              the extension .DAT.
# ChangeLog (Who,When,What):
#                            Robert Hiatt, 3/2/2021, Script & Assignment Completion
# --------------------------------------------------------------------------------- #

# --------------------------------------------------------------------------------- #
# Import the pickle module that allows for pickling data into a binary file.

import pickle

# --------------------------------------------------------------------------------- #
# Initialize variables.

lstTable =[]
choice = ""

# --------------------------------------------------------------------------------- #
# If there's a file on record, then the list will print below. Otherwise, a message
# appears telling the user to begin recording their characters.

# --------------------------------------------------------------------------------- #
# Introduce your program!

print()
print("Welcome to the Pickle Rick program! You can track characters you love and enter a general affinity for them!\n")
print("First let's see if you've already started a list.")

# --------------------------------------------------------------------------------- #
# If a file exists, message 1; else, run except message.

try:
    objFile = open("Assignment07.dat", "rb")
    objFileData = pickle.load(objFile)
    for i in objFileData:
        print(i["Character"] + " | " + i["Affinity"])
    objFile.close()
    print()
    print("Ah, I see you've been pickling!")

except FileNotFoundError as e:
    print()
    print("No file found. Let's start to pickle!")

# --------------------------------------------------------------------------------- #
# Loop through dictionary creation. Provide options to continue the program or to
# exit the program. Use structured error handling in case the user strays from their
# choice options.

print()
while choice != 'leave':
    character = str(input('What is the character\'s name?: '))
    affinity = str(input('What is the character\'s affinity?\n(Entering anything other than '
                         'these three options will fail to record your affinity.)\n'
                         'Options: love, like, or indifferent: '))
    dicRow = {"Character": character, "Affinity": affinity}
    lstTable.append(dicRow)
    try:
        choice = input("\nType 'leave' to skedaddle or 'more' to input another character: ").lower()
        if choice not in ['leave', 'more']:
           raise Exception("Use 'leave' or 'more' to get this program working! "
                           "You must want to enter another character.\n")
    except Exception as e:
        print()
        print("As I said: ", e)
# --------------------------------------------------------------------------------- #
# When the user decides to leave the program, the pickle funtion dump writes the
# pickled version of the object to the file.

print()
print("Throwing your entries into the pickling brine. Mmm...")
objFile = open("Assignment07.dat", "wb")
pickle.dump(lstTable, objFile)
objFile.close()

print()
print("You've done it! You created a program to capture characters and your affinity for them!\n")

# --------------------------------------------------------------------------------- #
# Recapitulate data entry for user peace of mind.

print("Here's what you pickled, by the way:\n")
objFile = open("Assignment07.dat", "rb")
objFileData = pickle.load(objFile)
for i in objFileData:
    print(i["Character"] + " | " + i["Affinity"])
objFile.close()

print()
print(input("Now press 'Enter' to close the program and skedaddle."))