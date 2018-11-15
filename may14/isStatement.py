import sys
#There block prints a message in case user forguets to input file
if len(sys.argv) < 2:
    print("\n Please enter the name of the file to be searched, after your script file name \n")
    sys.exit(1)
else:
    #Declaration of variables and opening of files for reading lines
    file = open(sys.argv[1], 'r')
    strings = file.readlines()

    statementBraker = ["?", "what", "What", "Where", "How", "how", "why","Why", "who", "Who","when",'?',"her." ,"When", "he", "He", "she", "She", "It", "it", " X ", " Y ", "they", "They"]


    for x in strings:
        y=x.split()
        print(" ")
        if len(y) <2:
            print(x[:-1]+" NOT STATEMENT")
            continue
        if "?" in x:
            print(x[:-1]+" NOT STATEMENT")
            continue

        for k in y:
            if k in statementBraker:
                print(x[:-1]+" NOT STATEMENT")
                break
        else:
            print(x[:-1]+" STATEMENT")
