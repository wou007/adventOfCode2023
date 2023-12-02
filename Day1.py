import re
import HelperFunctions

day_number = 1

def Part1(input):
    result = 0

    for line in input.splitlines():
        result += int(re.sub(r"\D","",line)[0] + re.sub(r"\D","",line)[-1])
    
    return result

def Part2(input):
    result = 0

    for line in input.splitlines():
        line = re.sub("one", "o1e", line)
        line = re.sub("two", "t2o", line)
        line = re.sub("three", "t3e", line)
        line = re.sub("four", "f4r", line)
        line = re.sub("five", "f5e", line)
        line = re.sub("six", "s6x", line)
        line = re.sub("seven", "s7n", line)
        line = re.sub("eight", "e8t", line)
        line = re.sub("nine", "n9e", line)
        
        result += int(re.sub(r"\D","",line)[0] + re.sub(r"\D","",line)[-1])
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')