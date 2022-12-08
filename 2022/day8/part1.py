
def main(grid):
    ans = 0
    gridWidth = len(grid[0])
    gridHeight = len(grid)

    for ypos, row in enumerate(grid):
        for xpos, treeHeight in enumerate(row):
            #checking horizontally
            if  all(grid[ypos][x] < treeHeight for x in range(0, xpos)):
                ans += 1
            elif all(grid[ypos][x] < treeHeight for x in range(xpos + 1, gridWidth)):
                ans += 1
            #checking vertically
            elif all(grid[y][xpos] < treeHeight for y in range(0, ypos)):
                ans += 1
            elif all(grid[y][xpos] < treeHeight for y in range(ypos + 1, gridHeight)):
                ans += 1
           
    print(ans)


def readInput():
    with open("input.txt", "r") as f:
       return f.read().splitlines()


if __name__ == "__main__":
    main(readInput())


