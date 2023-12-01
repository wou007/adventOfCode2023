import time

import HelperFunctions

import Day1

if __name__ == "__main__":
    days = [Day1]
    
    for d in days:
        input = HelperFunctions.ReadInput(d.day_number)

        if input != None:
            startTime = time.time()
            result1 = d.Part1(input)
            part1Time = time.time() - startTime
                            
            startTime = time.time()
            result2 = d.Part2(input)
            part2Time = time.time() - startTime

            print(f'Day {d.day_number}') 
            print(f'    Duration part 1 {round(part1Time,3)}s       Answer: {result1}')
            print(f'    Duration part 2 {round(part2Time,3)}s       Answer: {result2}\n')
        else:
            print(f'Day {d.day_number} NO INPUT\n')