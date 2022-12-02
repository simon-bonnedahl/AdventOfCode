def main(input):
    win = 6
    draw = 3
    rock = 1
    paper = 2
    scissors = 3
    totalScore = 0
    print(input)
    for line in input:
        
        opponent = line[0]
        you = line[1]

        if you == 'X':
            totalScore += rock
            if opponent == 'C':
                totalScore += win
            elif opponent == 'A':
                totalScore += draw
        elif you == 'Y':
            totalScore += paper
            if opponent == 'A':
                totalScore += win
            elif opponent == 'B':
                totalScore += draw
        elif you == 'Z':
            totalScore += scissors
            if opponent == 'B':
                totalScore += win
            elif opponent == 'C':
                totalScore += draw
    print(totalScore)



def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1].split(" ") for c in lines]

if __name__ == "__main__":
    main(readInput())