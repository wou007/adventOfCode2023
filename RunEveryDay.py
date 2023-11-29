import time

import Day1.Day1 as Day1

if __name__ == "__main__":
    days = [Day1]
    
    for d in days:
        input = d.ReadInput()

        startTime = time.time()
        d.Part1(input)
        part1Time = time.time() - startTime
                          
        startTime = time.time()
        d.Part2(input)
        part2Time = time.time() - startTime

        print(f'Day {d.day_number}') 
        print(f'Duration part 1 {round(part1Time,3)}s')
        print(f'Duration part 2 {round(part2Time,3)}s\n')