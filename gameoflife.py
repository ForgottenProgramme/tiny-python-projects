# Conway's Game of Life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list of list for cells:
nextCells = []
for x in range(WIDTH):
    column = [] # create new column
    for y in range(HEIGHT):
        if random.randint(0,1)==0:
            column.append('#') # Add a living cell
        else:
            column.append('') # Add a dead cell.
        
    nextCells.append(column) # nextCells is a list of column lists.

while True: # Main program loop.
    print("\n\n\n\n\n") # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() # print a newline at the end of the row.

    # Calculate the next step's cells based on current's.
