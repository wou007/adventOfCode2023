import os
import sys

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
import HelperFunctions  # Replace "my_module" here with the module name.
sys.path.pop(0)

day_number = 0

def Part1(input):
    result = 0

    for line in input.splitlines():
        line
    
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