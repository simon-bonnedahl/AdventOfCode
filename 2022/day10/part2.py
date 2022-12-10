def main(input):
    x = 1
    cycle = 0

    print()

    def nextCycle():
        nonlocal cycle
        if cycle % 40 in (x - 1, x, x + 1):
            print("#", end="")
        else:
            print(".", end="")
        cycle += 1
        if cycle % 40 == 0:
            print()

    for line in input:
        match line.split():
            case ["addx", num]:
                nextCycle()
                nextCycle()
                x += int(num)
            case ["noop"]:
                nextCycle()

def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    main(readInput())

