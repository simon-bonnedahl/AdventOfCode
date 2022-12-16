def main(input):
    blockedTiles = set()
    abyssDepth = 0

    for line in input:
        # Create full rockpath
        rockPath = []
        tiles = line.strip().split(" -> ")
        for tile in tiles:
            rockPath.append(list(map(int, tile.split(","))))
           
        #Add all of the tiles in the rockpath to the blocked tiles
        for (x1, y1), (x2, y2) in zip(rockPath, rockPath[1:]):
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    blockedTiles.add((x, y))
                    abyssDepth = max(abyssDepth, y + 1)

    sum = 0
    while (500, 0) not in blockedTiles:
        sandSrc = (500, 0)
        while True:
            if sandSrc[1] >= abyssDepth:
                break
            #Check down
            if (sandSrc[0], sandSrc[1] + 1) not in blockedTiles:
                sandSrc = (sandSrc[0], sandSrc[1] + 1)
                continue
            #Check downleft
            if (sandSrc[0] - 1, sandSrc[1] + 1) not in blockedTiles:
                sandSrc = (sandSrc[0] - 1, sandSrc[1] + 1)
                continue
            #Check downright
            if (sandSrc[0] + 1, sandSrc[1] + 1) not in blockedTiles:
                sandSrc = (sandSrc[0] + 1, sandSrc[1] + 1)
                continue
            break
        blockedTiles.add(sandSrc)
        sum += 1
    print(sum)  


def readInput():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    main(readInput())
