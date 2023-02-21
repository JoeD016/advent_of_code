import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def main():
    # input via .txt file
    with open('input1.txt') as f:
        lines = f.read().splitlines()
    ins, val = '', 0
    cycleCount = 0
    cache = {20, 60, 100, 140, 180, 220}
    res, currentVal = 0, 1
    for line in lines:
        instruction = line.split(' ')
        if len(instruction) == 2:
            ins, val = instruction
            val = int(val)
            cycleCount += 1
            if cycleCount in cache:
                # print(f'cycle {cycleCount}, value {currentVal}, instruction {ins}')
                res += cycleCount * currentVal
            cycleCount += 1
            if cycleCount in cache:
                # print(f'cycle {cycleCount}, value {currentVal}, instruction {ins}')
                res += cycleCount * currentVal
            currentVal += val
        else:
            ins = instruction[0]
            cycleCount += 1
            if cycleCount in cache:
                # print(f'cycle {cycleCount}, value {currentVal}, instruction {ins}')
                res += cycleCount * currentVal
    print(res)


if __name__ == "__main__":
    main()