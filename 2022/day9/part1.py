
def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

    

def diff(t1, t2):
    diffx = (t1[0] - t2[0])
    diffy = (t1[1] - t2[1])
    x = min(1, max(-1, diffx))
    y = min(1, max(-1, diffy))
    return (x, y)

def main(input):
    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add(tail)
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    

    for line in input:
         direction, length = line.split()

         for _ in range(int(length)):
            head = add(head, directions[direction])
            d = diff(head, tail)
            if head[0] - tail[0] == d[0] and head[1] - tail[1] == d[1]:
               continue
            else:
                tail = (tail[0] + d[0],  tail[1] + d[1])
                
                
            visited.add(tail)
    print(len(visited))

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
    return lines

if __name__ == "__main__":
    main(readInput())





         
