def main(input):
    sum = 0
    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    while(i < len(input)):
        for c in input[i]:
            if c in input[i + 1] and c in input[i + 2]:
                sum += alphabet.find(c)
                break
        i+=3
    print(sum)
        

def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]

if __name__ == "__main__":
    main(readInput())