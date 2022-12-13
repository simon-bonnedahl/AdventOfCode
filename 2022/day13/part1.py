
def compare(left, right):
    if type(left) == int:
        if type(right) == int:
            #If both are int
            return left - right
        else:
            #if left is int and right is list
            return compare([left], right)
    else:
        if type(right) == int:
            #if right is int and left is list
            return compare(left, [right])

    #if both are lists
    
    for a, b in zip(left, right):
            if compare(a, b) == 0:
                continue
            return compare(a, b)

    return len(left) - len(right)

def main(input):
    sum = 0
    packets = list(map(str.splitlines, input.strip().split("\n\n")))
    for index, (left, right) in enumerate(packets):
        if compare(eval(left), eval(right)) < 0:
            sum += (index + 1)
    
    print(sum)     

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read()
    return lines

if __name__ == "__main__":
    main(readInput())

