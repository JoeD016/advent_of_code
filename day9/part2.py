import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def distance(prev,current):
    prevX, prevY = prev
    currentX, currentY = current
    return abs(prevY - currentY) + abs(prevX - currentX)

def moveCurrent(prev,current):
    dist = distance(prev,current)
    if dist < 2:
        return current
    prevX, prevY = prev
    currentX, currentY = current
    if prevX == currentX and dist == 2:
        currentY += (prevY - currentY) // 2
    elif prevY == currentY and dist == 2:
        currentX += (prevX - currentX) // 2
    elif dist == 2:
        return current
    else:
        currentY += (prevY - currentY) * abs(1/(prevY - currentY))
        currentX += (prevX - currentX) *abs(1/(prevX - currentX))
    return [currentX,currentY]


def main():
    # input via .txt file
    with open('input2.txt') as f:
        lines = f.read().splitlines()
    directions = {"L":(-1,0), "R":(1,0), "U":(0,-1), "D":(0,1)}
    instructions = []
    for line in lines:
        ins = line.split(' ')
        instructions.append(ins)
    
    status = [[0,0] for _ in range(10)]
    cache = set()
    for direction, steps in instructions:
        for _ in range(int(steps)):
            move = directions[direction]
            head = status[0]
            head[0] += move[0]
            head[1] += move[1]
            for i in range(1,10):
                prev = status[i - 1]
                current = status[i]
                status[i] = moveCurrent(prev,current)
                if i == 9:
                    cache.add(tuple(status[i]))
            
    print(len(cache))


if __name__ == "__main__":
    main()