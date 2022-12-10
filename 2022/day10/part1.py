

def main(input):
    x = 1
    cycle = 0
    cycles = [20, 60, 100, 140, 180, 220]
    signalStrength = 0
    

    def nextCycle():
        nonlocal cycle, signalStrength
        cycle += 1
        if cycle in cycles:
            signalStrength += cycle * x

    for line in input:
        match line.split():
            case ["addx", num]:
                nextCycle()
                nextCycle()
                x += int(num)
            case ["noop"]:
                nextCycle()

    print(signalStrength)


def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    main(readInput())
    p2(readInput())

