import sys
import HelperFunctions
import re

day_number = 2

def Part1(input):
    result = 0

    for line in input.splitlines():
        res = re.search(r"Game (\d+):",line)
        game = int(res.group(1))
        possible = True

        res = re.findall(r"(\d+) (blue|green|red)", line)
        for i in res:
            if i[1] == 'red':
                if int(i[0]) > 12:
                    possible = False
                    break
            if i[1] == 'green':
                if int(i[0]) > 13:
                    possible = False
                    break
            if i[1] == 'blue':
                if int(i[0]) > 14:
                    possible = False
                    break

        if possible:
            result += game

    return result

def Part2(input):
    result = 0

    for line in input.splitlines():        
        r = 1
        g = 1
        b = 1

        res = re.findall(r"(\d+) (blue|green|red)", line)
        for i in res:
            if i[1] == 'red':
                r = max(r,int(i[0]))
            if i[1] == 'green':
                g = max(g,int(i[0]))
            if i[1] == 'blue':
                b = max(b,int(i[0]))

        result += r * g * b

    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')