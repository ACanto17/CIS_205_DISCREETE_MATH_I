import sys

def drawRow(numSpaces, numStars):
    spaces = " " * numSpaces
    stars = "*" * numStars
    finalString = spaces + stars
    print(finalString)

# drawRow(5,1)
# drawRow(2,8)
# drawRow(0,3)



def drawPyrmaid(height):
    for i in range(0, height):
        drawRow(height-i,1+i*2)

# drawPyrmaid(5)

drawPyrmaid(int(sys.argv[1]))
