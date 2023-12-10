import sys
import HelperFunctions
import re

day_number = 9

def Part1(input):
    result = 0

    results = []

    for line in input.splitlines():
        numbers = []
        numbers.append([int(n) for n in re.findall(r"(-?\d+)",line)])

        while len(numbers[-1]) != numbers[-1].count(0):
            newLine = []
            currLine = numbers[-1]
            for i in range(1, len(currLine)):
                newLine.append(currLine[i]-currLine[i-1])
            numbers.append(newLine)
        
        res = 0

        for l in range(len(numbers) - 1,-1, -1):
            res += numbers[l][-1]

        results.append(res)
    
    result = sum(results)

    return result

def Part2(input):
    result = 0

    for line in input.splitlines():
        line
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')