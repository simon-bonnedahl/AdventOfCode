def main(input):
    for i in range(len(input) - 4):
        if len(set(input[i-4:i])) == 4:
            print(i)
            break

def readInput():
    with open("input.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    main(readInput())