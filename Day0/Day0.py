import os

day_number = 0

def Part1(input):
    result = 0

    for line in input.splitlines():
        print(line)
    
    print(f'Part 1: {result}')

def Part2(input):
    result = 0

    for line in input.splitlines():
        print(line)
    
    print(f'Part 2: {result}')

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
    Part1(input)
    Part2(input)

if __name__ == "__main__":
    Run()