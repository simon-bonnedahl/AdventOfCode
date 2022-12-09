
def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def diff(t1, t2):
    diffx = (t1[0] - t2[0])
    diffy = (t1[1] - t2[1])
    x = min(1, max(-1, diffx))
    y = min(1, max(-1, diffy))
    return (x, y)

def main(input):
    tail = (0, 0)
    history = [(0, 0) for _ in range(10)]

    visited = set()
    visited.add(tail)
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    

    for line in input:
         direction, length = line.split()

         for _ in range(int(length)):
            history[0] = add(history[0], directions[direction])
            for i in range(len(history) - 1):

                d = diff(history[i], history[i + 1])
                if history[i][0] - history[i + 1][0] == d[0] and history[i][1] - history[i + 1][1] == d[1]:
                    continue
                else:
                    history[i + 1] = (history[i + 1][0] + d[0],  history[i + 1][1] + d[1])
                visited.add(history[9])                        
            

    print(len(visited))
    

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    return lines

if __name__ == "__main__":
    main(readInput())





         
