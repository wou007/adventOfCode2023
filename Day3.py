import sys
import HelperFunctions
import Matrix

day_number = 3

numbers = ['0','1','2','3','4','5','6','7','8','9']
notSymbols = ['0','1','2','3','4','5','6','7','8','9','.']

def Part1(input):
    result = 0

    m = Matrix.Matrix()
    m.FromInput(input)

    for row in range(m.GetHeight()):
        number = ''
        startFound = False
        symbolFound = False
        for c in range(m.GetWidth()):
            if m.GetPixel(c,row) in numbers:
                number += m.GetPixel(c,row)
                startFound = True
                for n in m.GetNeighborsOf(c,row,True):
                    if m.GetPixel(n[0],n[1]) not in notSymbols:
                        symbolFound = True
            elif startFound:
                if symbolFound:
                    result += int(number)
                number = ''
                symbolFound = False
                startFound = False
        if startFound:
            if symbolFound:
                result += int(number)
            number = ''
            symbolFound = False
            startFound = False
    
    return result

def Part2(input):
    result = 0

    m = Matrix.Matrix()
    m.FromInput(input)

    gearsWithNumbers = {}

    for row in range(m.GetHeight()):
        number = ''
        startFound = False
        gearFound = None
        for c in range(m.GetWidth()):
            if m.GetPixel(c,row) in numbers:
                number += m.GetPixel(c,row)
                startFound = True
                for n in m.GetNeighborsOf(c,row,True):
                    if m.GetPixel(n[0],n[1]) == '*':
                        gearFound = n
            elif startFound:
                if gearFound != None:
                    if str(gearFound) in gearsWithNumbers:
                        gearsWithNumbers[str(gearFound)].append(int(number))
                    else:
                        gearsWithNumbers[str(gearFound)] = [int(number)]
                number = ''
                gearFound = None
                startFound = False
        if startFound:
            if gearFound != None:
                if str(gearFound) in gearsWithNumbers:
                    gearsWithNumbers[str(gearFound)].append(int(number))
                else:
                    gearsWithNumbers[str(gearFound)] = [int(number)]
            number = ''
            gearFound = None
            startFound = False

    for key, value in gearsWithNumbers.items():
        if len(value) == 2:
            result += value[0] * value[1]
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')