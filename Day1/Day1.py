import sys
import re

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
import HelperFunctions  # Replace "my_module" here with the module name.
sys.path.pop(0)

day_number = 1

def Part1(input):
    result = 0

    for line in input.splitlines():
        l = re.sub("\D","",line)[0] + re.sub("\D","",line)[-1]
        result = result + int(l)
    
    return result

def Part2(input):
    result = 0

    for line in input.splitlines():
        line.find("one")
        line = re.sub("eight", "e8t", line)
        line = re.sub("two", "t2o", line)
        line = re.sub("one", "o1e", line)
        line = re.sub("three", "t3e", line)
        line = re.sub("four", "f4r", line)
        line = re.sub("five", "f5e", line)
        line = re.sub("six", "s6x", line)
        line = re.sub("seven", "s7n", line)
        line = re.sub("nine", "n9e", line)
        
        l = re.sub("\D","",line)[0] + re.sub("\D","",line)[-1]

        result = result + int(l)
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')