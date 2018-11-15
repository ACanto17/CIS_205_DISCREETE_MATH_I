import sys


#There block prints a message in case user forguets to input file
if len(sys.argv) < 2:
    print("\n Please enter the name of the file to be searched, after your script file name \n")
    sys.exit(1)

else:
    #Declaration of variables and opening of files for readind
    file = open(sys.argv[1], 'r')
    strings = file.readlines()
    numberOfElements = 0
    elementToCount = "8"

# Here the program loops through every line of the given text and counts the 8's
    for i in range(0, len(strings)):
        numberOfElements += strings[i].count(elementToCount)

#Here the code prints the final result
    print("\n Number of 8's:")
    print(numberOfElements)
