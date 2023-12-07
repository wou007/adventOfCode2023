import sys
import HelperFunctions
import re
import threading
import multiprocessing

day_number = 5

def Part1(input):
    result = 999999999999999

    splits = input.splitlines()

    seeds = re.findall(r"(\d+)",splits[0])

    maps = []
    tempMap = []
    for line in splits[3::]:
        a = re.findall(r"(\d+)",line)
        if len(a) == 3:
            tempMap.append(a)
        elif len(tempMap) > 0:
            maps.append(tempMap)
            tempMap = []
    if len(tempMap) > 0:
        maps.append(tempMap)
        tempMap = []

    conversions = []
    tempConversions = []
    for a in maps:
        for b in a:
            start = int(b[1])
            end = int(b[1]) + int(b[2]) - 1
            operation = int(b[0]) - int(b[1]) 
            tempConversions.append([start,end,operation])
        conversions.append(tempConversions)
        tempConversions=[]

    for s in seeds:
        l = int(s)
        for c in conversions:
            for x in c:
                if l >= x[0] and l <= x[1]:
                    l += x[2]
                    break
        result = min(result, l)
            
    
    return result

def StepsToSkip(a, conversionList):
    # List must be sorted
    for c in conversionList:
        if c[0] <= a and c[1] > a: # in range
            return (c[1] - a) + 1
        elif c[0] > a:  # before any conversion
            return c[0] - a
    return sys.maxsize

def Part2(input):
    result = 999999999999999

    splits = input.splitlines()

    seeds =[eval(i) for i in re.findall(r"(\d+)",splits[0])]

    maps = []
    tempMap = []
    for line in splits[3::]:
        a = re.findall(r"(\d+)",line)
        if len(a) == 3:
            tempMap.append(a)
        elif len(tempMap) > 0:
            maps.append(tempMap)
            tempMap = []
    if len(tempMap) > 0:
        maps.append(tempMap)
        tempMap = []

    conversions = []
    tempConversions = []
    for a in maps:
        for b in a:
            start = int(b[1])
            end = int(b[1]) + int(b[2]) - 1
            operation = int(b[0]) - int(b[1]) 
            tempConversions.append([start,end,operation])
        conversions.append(tempConversions)
        tempConversions=[]

    for c in conversions:
        c.sort()

    for s in range(0,len(seeds),2):
        seed = seeds[s]
        while seed < seeds[s] + seeds[s+1]:
            stepsToSet = sys.maxsize
            l = seed
            for c in conversions:
                stepsToSet = min(stepsToSet, StepsToSkip(l, c))
                for x in c:
                    if l >= x[0] and l <= x[1]:
                        l += x[2]
                        break
            result = min(result, l)
            seed += max(1,stepsToSet)
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')