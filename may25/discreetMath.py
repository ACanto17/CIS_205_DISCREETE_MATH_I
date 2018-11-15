# Helper funciton to search coincidences
def searchCOuncidences(listToSearch,listOfElementsToSearch):
    for i in range(len(listToSearch)):
        try:
            newIndexOfCoincidence = listToSearch.index(listOfElementsToSearch[i])
        except ValueError:
            continue
        except IndexError:
            continue

        indexesInCoincidence.append(newIndexOfCoincidence)
    print("Indexes of coincidences of"+indexesInCoincidence)


import sys
#There block prints a message in case user forguets to input file
if len(sys.argv) < 2:
    print("\n Please enter the name of the file to be searched, after your script file name \n")
    sys.exit(1)
else:
    #Declaration of variables and opening of files for reading lines
    file = open(sys.argv[1], 'r')
    statements = file.readlines()
    A = statements[0].rstrip()
    B = statements[1].rstrip()
    arrayA = statements[0].split()
    arrayB = statements[1].split()
    indexesInCoincidence =[]
    AunionB =[]
    tempB=[]


#  Print set A in notation
    finalString = ('{'+A+'}')
    print(finalString)

#  Print set B in notation
    finalString = ('{'+B+'}')
    print(finalString)

#   searchCOuncidences
    searchCOuncidences(arrayA,arrayB)
    AunionB.append(arrayA)
    tempB.append(arrayB)

    for i in indexesInCoincidence:
        tempB.remove(tempB[i])

    tempB.append()

    print(tempB)
