import sys
import HelperFunctions
import re
import math

day_number = 8

def Part1(input):
    result = 0

    LR = input.splitlines()[0]
    nodes = {}
    for line in input.splitlines()[2::]:
        splits = re.findall(r"([A-Z]{3})",line)
        nodes[splits[0]] = [splits[1], splits[2]]

    currNode = 'AAA'
    step = 0
    while currNode != 'ZZZ':
        direction = 0 if LR[step % len(LR)] == 'L' else 1
        currNode = nodes[currNode][direction]
        step += 1

    result = step
    
    return result

def Part2(input):
    result = 1

    LR = input.splitlines()[0]
    nodes = {}
    startNodes = []
    for line in input.splitlines()[2::]:
        splits = re.findall(r"([A-Z]{3})",line)
        nodes[splits[0]] = [splits[1], splits[2]]
        if splits[0][2] == 'A':
            startNodes.append(splits[0])

    times = []

    for s in startNodes:
        currNode = s
        step = 0
        while currNode[2] != 'Z':
            direction = 0 if LR[step % len(LR)] == 'L' else 1
            currNode = nodes[currNode][direction]
            step += 1
        times.append(step)

    for t in times:
        result = math.lcm(t,result)
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')