def main(input):
    sum = 0
    for pair in input:
        e1, e2 = pair.split(",")
        e1_start, e1_end = map(int, e1.split("-"))
        e2_start, e2_end = map(int, e2.split("-"))
        e1_set = set(range(e1_start, e1_end + 1))
        e2_set = set(range(e2_start, e2_end + 1))
        if len(e1_set - e2_set) == 0 or len(e2_set - e1_set) == 0:
            sum += 1

    print(sum)

        

def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]

if __name__ == "__main__":
    main(readInput())