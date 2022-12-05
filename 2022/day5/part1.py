def main(input):
    #Manual input of the stacks
    """     [V] [G]             [H]        
        [Z] [H] [Z]         [T] [S]        
        [P] [D] [F]         [B] [V] [Q]    
        [B] [M] [V] [N]     [F] [D] [N]    
        [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
        [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
        [D] [L] [H] [G] [F] [Q] [M] [G] [W]
        [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
        1   2   3   4   5   6   7   8   9 
    """
    stacks = [
        list("ZPBQMDN"[::-1]),
        list("VHDMQZLC"[::-1]),
        list("GZFVDRHQ"[::-1]),
        list("NFDGH"[::-1]),
        list("QFN"[::-1]),
        list("TBFZVQD"[::-1]),
        list("HSVDZTMQ"[::-1]),
        list("QNPFGM"[::-1]),
        list("MRWB"[::-1]),
    ]

    for line in input:
    #  move   x   from  y  to  z
        _, amount, _, src, _, dest = line.split(" ")

        amount = int(amount)
        src = int(src) -1
        dest = int(dest) -1

        stack = stacks[src]
        crates = stack[-amount:]            #create the moving crates

        stacks[src] = stacks[src][:-amount] #Remove the moving crates from the source
        for c in reversed(crates):
            stacks[dest] = stacks[dest] + [c] #Add them to the destionation stack in reversed order
       
    res = ""
    for c in stacks:
        res += c[-1]
 
    print(res)

        

def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return [c[:-1] for c in lines]

if __name__ == "__main__":
    main(readInput())





         
