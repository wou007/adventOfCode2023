import os

day_number = 1

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

def ReadInput():
    filePath = ''
    if os.path.isfile('input.txt'):
        filePath = 'input.txt'
    elif os.path.isfile(f'Day{day_number}/input.txt'):
        filePath = f'Day{day_number}/input.txt'
    
    file = open(filePath, 'r')
    data = file.read()
    file.close()

    return data

def Run():
    print(f'Day {day_number}')
    input = ReadInput()
    print(f'Part 1: {Part1(input)}')
    print(f'Part 2: {Part2(input)}')

if __name__ == "__main__":
    Run()