from math import prod
def main(grid):
    scores = []
    gridWidth = len(grid[0])
    gridHeight = len(grid)

    for ypos, row in enumerate(grid):
        for xpos, treeHeight in enumerate(row):
                        #left up right down
            visibleTrees = [0, 0, 0, 0]
            #left
            for x in range(xpos - 1, -1, -1):
                visibleTrees[0] += 1
                if grid[ypos][x] >= treeHeight: #if we get blocked sight we stop couting
                    break
            #up
            for y in range(ypos - 1, -1, -1):
                visibleTrees[1] += 1
                if grid[y][xpos] >= treeHeight:
                    break
            #right
            for x in range(xpos + 1, gridWidth):
                visibleTrees[2] += 1
                if grid[ypos][x] >= treeHeight:
                    break
            #down
            for y in range(ypos + 1, gridHeight):
                visibleTrees[3] += 1
                if grid[y][xpos] >= treeHeight:
                    break
            
            scores.append(prod(visibleTrees))

    print(max(scores))

def readInput():
    with open("input.txt", "r") as f:
       return f.read().splitlines()

if __name__ == "__main__":
    main(readInput())





         
