
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
    divider_2 = 1
    divider_6 = 2

    packets = list(map(eval, input.split()))
    for packet in packets:
        #Normal packet
        if compare(packet, [[2]]) < 0:
            divider_2 += 1
            divider_6 += 1
        elif compare(packet, [[6]]) < 0:
            divider_6 += 1
        else:
            #Divider packet
            continue
    print(divider_2 * divider_6)

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read()
    return lines

if __name__ == "__main__":
    main(readInput())
