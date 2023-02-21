import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def main():
    # input via .txt file
    with open('input2.txt') as f:
        lines = f.read().splitlines()
    ins, val = '', 0
    cycleCount = 0
    CRT, currentVal = [], 1
    distant = {39, 0, 1}
    for line in lines:
        instruction = line.split(' ')
        if len(instruction) == 2:
            _, val = instruction
            val = int(val)

            if (abs(cycleCount - currentVal) % 40) in distant:
                CRT.append('#')
            else:
                CRT.append('.')
            cycleCount += 1
            
            if (abs(cycleCount - currentVal) % 40) in distant:
                CRT.append('#')
            else:
                CRT.append('.')
            cycleCount += 1
            
            currentVal += val
        else:
            ins = instruction[0]
            if (abs(cycleCount - currentVal) % 40) in distant:
                CRT.append('#')
            else:
                CRT.append('.')
            cycleCount += 1
            
    CRT = [CRT[i:i+40] for i in range(0, 240, 40)]
    for line in CRT:
        print(''.join(line))


if __name__ == "__main__":
    main()