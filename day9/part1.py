import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def distance(head,tail):
    headX, headY = head
    tailX, tailY = tail
    return abs(headY - tailY) + abs(headX - tailX)

def moveTail(head,tail):
    dist = distance(head,tail)
    if dist < 2:
        return tail
    headX, headY = head
    tailX, tailY = tail
    if headX == tailX and dist == 2:
        tailY += (headY - tailY) // 2
    elif headY == tailY and dist == 2:
        tailX += (headX - tailX) // 2
    elif dist == 2:
        return tail
    else:
        tailY += (headY - tailY) * abs(1/(headY - tailY))
        tailX += (headX - tailX) *abs(1/(headX - tailX))
    return [tailX,tailY]


def main():
    # input via .txt file
    with open('input1.txt') as f:
        lines = f.read().splitlines()
    directions = {"L":(-1,0), "R":(1,0), "U":(0,-1), "D":(0,1)}
    instructions = []
    for line in lines:
        ins = line.split(' ')
        instructions.append(ins)
    
    head, tail = [0,0], [0,0]
    cache = set()
    for direction, steps in instructions:
        for _ in range(int(steps)):
            move = directions[direction]
            head[0] += move[0]
            head[1] += move[1]
            tail = moveTail(head,tail)
            cache.add(tuple(tail))
    print(len(cache))


if __name__ == "__main__":
    main()