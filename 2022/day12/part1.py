from collections import deque

def main(input):

    grid = [list(c) for c in input.strip().splitlines()]

    def getNeighbors(pos):
        neighbors = []
        neighbors.append((pos[0], pos[1] + 1)) # down
        neighbors.append((pos[0], pos[1] - 1 )) # up
        neighbors.append((pos[0] + 1, pos[1])) # right
        neighbors.append((pos[0] - 1, pos[1])) # left
        return neighbors

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "S":
                src = (x, y)
                grid[y][x] = "a"
            if char == "E":
                dst = (x, y)
                grid[y][x] = "z"

    q = deque()
    q.append([0, src])

    visited = set()
    visited.add(src)

 

    #BFS
    while q:
        distance, pos = q.popleft()
        for neighbor in getNeighbors(pos):
            #Check grid bounds      
            if neighbor[0] < 0 or neighbor[1] < 0:      #X
                continue   
            if neighbor[0] >= len(grid[0]) or neighbor[1] >= len(grid): #Y
                continue   
            #Check visited
            if neighbor in visited:
                continue
            #Check elevation diff
            if ord(grid[neighbor[1]][neighbor[0]]) - ord(grid[pos[1]][pos[0]]) > 1:
                continue
            #Check if we found the destionation
            if neighbor == dst:
                print(distance + 1)
                exit()
                
            #Add neighbor to the queue
            visited.add(neighbor)
            q.append([distance + 1, neighbor])


           

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read()
    return lines

if __name__ == "__main__":
    main(readInput())

