def main(input):
    monkeys = []

    for section in input.strip().split("\n\n"):
        lines = section.splitlines()
        monkey = {}
        monkey['items'] = list(map(int, lines[1].split(": ")[1].split(", ")))
        f = "lambda old:" + lines[2].split("=")[1]
        monkey['operation'] =  eval(f)
        monkey['divisible'] = int(lines[3].split()[-1])
        monkey['true'] = int(lines[4].split()[-1])
        monkey['false'] = int(lines[5].split()[-1])
        monkeys.append(monkey)

    inspections = [0 for i in range(len(monkeys))]

    for _ in range(20):
        for index, monkey in enumerate(monkeys):
            for item in monkey['items']:
                item = monkey['operation'](item)
                item = item // 3
                if item % monkey['divisible'] == 0:
                    monkeys[monkey['true']]['items'].append(item)
                else:
                    monkeys[monkey['false']]['items'].append(item)
            inspections[index] += len(monkey['items'])
            monkey['items'] = []

    inspections.sort()
    monkeyBusiness = inspections[-1] * inspections[-2]
    print(monkeyBusiness)

def readInput():
    with open("input.txt", "r") as f:
        lines = f.read()
    return lines

if __name__ == "__main__":
    main(readInput())

