import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def getLeft(grid):
    n = len(grid)
    from_left = [[0] * n for _ in range(n)]
    for i in range(len(from_left)):
        heights = grid[i]
        row = from_left[i]
        for j in range(1, n):
            if j == 1:
                row[j] = 1
            else:
                if heights[j] > heights[j - 1]:
                    row[j] = 1
                    next = j - 1
                    while next > 0 and heights[j] > heights[next]:
                        row[j] += 1
                        next -= 1
                else:
                    row[j] = 1

    return from_left

def getTop(grid):
    n = len(grid)
    from_top = [[0] * n for _ in range(n)]
    for i in range(len(from_top)):
        heights = [row[i] for row in grid]
        for j in range(1, n):
            if j == 1:
                from_top[j][i] = 1
            else:
                if heights[j] > heights[j - 1]:
                    from_top[j][i] = 1
                    next = j - 1
                    while next > 0 and heights[j] > heights[next]:
                        from_top[j][i] += 1
                        next -= 1
                else:
                    from_top[j][i] = 1

    return from_top

def getBottom(grid):
    n = len(grid)
    from_bottom = [[0] * n for _ in range(n)]
    for i in range(len(from_bottom)):
        heights = [row[i] for row in grid]
        for j in range(n - 2, -1, -1):
            if j == n - 2:
                from_bottom[j][i] = 1
            else:
                if heights[j] > heights[j + 1]:
                    from_bottom[j][i] = 1
                    next = j + 1
                    while next < n - 1 and  heights[j] > heights[next]:
                        from_bottom[j][i] += 1
                        next += 1
                else:
                    from_bottom[j][i] = 1

    return from_bottom

def getRight(grid):
    n = len(grid)
    from_right = [[0] * n for _ in range(n)]
    for i in range(len(from_right)):
        heights = grid[i]
        row = from_right[i]
        for j in range(n - 2, -1, -1):
            if j == n - 1:
                row[j] = 1
            else:
                if heights[j] > heights[j + 1]:
                    row[j] = 1
                    next = j + 1
                    while next < n - 1 and  heights[j] > heights[next]:
                        row[j] += 1
                        next += 1
                else:
                    row[j] = 1

    return from_right

def main():
    # input via .txt file
    with open('input2.txt') as f:
        lines = f.read().splitlines()
    
    grid = []
    
    for line in lines:
        grid.append([int(digit) for digit in line])
    n = len(grid)
    left,right,top,bottom = getLeft(grid), getRight(grid), getTop(grid), getBottom(grid)
    res = 0
    for row in range(n):
        for col in range(n):
            res = max(res, left[row][col]*right[row][col]*top[row][col]*bottom[row][col])
    print(res)
    
    

            
    


if __name__ == "__main__":
    main()