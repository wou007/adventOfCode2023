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
            end = int(b[1]) + int(b[2])
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

def Part2ThreadingFunction(seeds, i, conversions):
    res = 999999999999999
    for v in range(int(seeds[i]),int(seeds[i]) + int(seeds[i+1])):
        l = v
        for c in conversions:
            for x in c:
                if l >= x[0] and l <= x[1]:
                    l += x[2]
                    break
        res = min(res, l)
    print(res)

def Part2(input):
    global result2
    result2 = 999999999999999

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
            end = int(b[1]) + int(b[2])
            operation = int(b[0]) - int(b[1]) 
            tempConversions.append([start,end,operation])
        conversions.append(tempConversions)
        tempConversions=[]

    threads = []

    for s in range(0,len(seeds),2):
        s = int(s)
        threads.append(multiprocessing.Process(target=Part2ThreadingFunction,args=(seeds,s,conversions)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()         
    
    return result2

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')