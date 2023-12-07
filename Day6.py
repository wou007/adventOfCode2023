import sys
import HelperFunctions
import re

day_number = 6

def Part1(input):
    result = 1

    lines = input.splitlines()
    times = re.findall(r"(\d+)",lines[0])
    distances = re.findall(r"(\d+)",lines[1])

    for i in range(len(times)):
        wins = 0
        time = int(times[i])
        distance = int(distances[i])
        for s in range((round(distance/time)),time):
            if s * (time - s) > distance:
                wins = time - (s * 2)
                break
        result *= wins

    
    return result

def Part2(input):
    result = 1

    input = input.replace(' ','')
    lines = input.splitlines()
    times = re.findall(r"(\d+)",lines[0])
    distances = re.findall(r"(\d+)",lines[1])

    for i in range(len(times)):
        wins = 0
        time = int(times[i])
        distance = int(distances[i])
        for s in range((round(distance/time)),time):
            if s * (time - s) > distance:
                wins = time - (s * 2)
                break
        result *= wins

    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')