def main(input):
    for i in range(len(input) - 14):
        if len(set(input[i-14:i])) == 14:
            print(i)
            break

def readInput():
    with open("input.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    main(readInput())