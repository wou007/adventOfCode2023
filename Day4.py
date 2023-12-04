import sys
import HelperFunctions

day_number = 4

def Part1(input):
    result = 0

    for line in input.splitlines():
        splits = line.split(': ')
        ab = splits[1].split(' | ')
        a = ab[0].split(" ")
        b = ab[1].split(" ")

        count = 0
        for i in b:
            if i != '' and i in a:
                count += 1

        if count > 0:
            result += 2**(count - 1)
    
    return result

def Part2(input):
    result = 0

    cardResults = []

    for line in input.splitlines():
        splits = line.split(': ')
        ab = splits[1].split(' | ')
        a = ab[0].split(" ")
        b = ab[1].split(" ")

        count = 0
        for i in b:
            if i != '' and i in a:
                count += 1

        cardResults.append(count)

    numbersOfCards = [1 for j in range(len(cardResults))]

    for i in range(len(numbersOfCards)):
        for j in range(cardResults[i]):
            numbersOfCards[i + j + 1] += numbersOfCards[i]
        result += numbersOfCards[i]
    
    return result

if __name__ == "__main__":
    print(f'Day {day_number}')
    input = HelperFunctions.ReadInput(day_number)
    if input != None:
        print(f'Part 1: {Part1(input)}')
        print(f'Part 2: {Part2(input)}')
    else:
        print(f'No input for day {day_number} found')