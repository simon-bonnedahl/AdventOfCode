def main(input):

    system = {}
    path = []
    
    for line in input:
        tokens = line.strip().split()
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                path.pop()
            else:
                path.append(tokens[2])
        elif tokens[1] == 'ls':
            continue
        elif tokens[0] == 'dir':
            continue
        else:
            size = int(tokens[0])
            for i in range(0, len(path)+1):
                dir = "".join(path[:i])
                if dir in system:
                      system[dir] += size
                else:
                    system[dir] = size
    sum = 0
    for dir, size in system.items():
        if size <= 100000:
            sum += size
    print(sum)

def readInput():
    with open("input.txt", "r") as f:
        d = f.read().strip()
    return [x for x in d.split('\n')]

if __name__ == "__main__":
    main(readInput())


