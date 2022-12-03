def main(input):
    
    sum = 0
    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
    for line in input:
        half = len(line)//2
        a = line[:half]
        b = line[half:]

        for c in a:
            if c in b:
                sum += alphabet.find(c)
                break
    print(sum)
        

def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]

if __name__ == "__main__":
    main(readInput())