def main(input):
    win = 6
    draw = 3
    rock = 1
    paper = 2
    scissors = 3
    totalScore = 0

    for line in input:
        opponent = line.split(" ")[0]
        outcome = line.split(" ")[1]

        if outcome == 'X':  #loss
            if opponent == 'A':
                totalScore += scissors
            elif opponent == 'B':
                totalScore += rock
            elif opponent == 'C':
                totalScore += paper
        elif outcome == 'Y':    #draw
            totalScore += draw
            if opponent == 'A':
                totalScore += rock
            elif opponent == 'B':
                totalScore += paper
            elif opponent == 'C':
                totalScore += scissors
        elif outcome == 'Z':    #win
            totalScore += win
            if opponent == 'A':
                totalScore += paper
            elif opponent == 'B':
                totalScore += scissors
            elif opponent == 'C':
                totalScore += rock
    print(totalScore)



def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]

if __name__ == "__main__":
    main(readInput())




    
