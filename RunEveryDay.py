import time

import HelperFunctions

import Day1
import Day2
import Day3
import Day4
import Day5
import Day6
import Day7
import Day8

if __name__ == "__main__":
    days = [Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8]
    
    totalStart = time.time()
    totalTime = 0
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
            print(f'    Duration part 1 {round(part1Time,3)}s\tAnswer: {result1}')
            print(f'    Duration part 2 {round(part2Time,3)}s\tAnswer: {result2}\n')

            totalTime += part1Time + part2Time
        else:
            print(f'Day {d.day_number} NO INPUT\n')

    print(f'Total Time: {round(time.time() - totalStart,3)} without IO: {round(totalTime,3)}s')