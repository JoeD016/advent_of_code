import math,string,collections

# import inbuilt standard input output
from sys import stdin, stdout

def getTrees(grid, i, cache, isRow):
    list = grid[i] if isRow else [row[i] for row in grid]
    n = len(list)
    cur_max = list[0]
    for j in range(1, n - 1):
        value = list[j]
        if value > cur_max:
            index = (i, j) if isRow else (j, i)
            cache.add(index)
            cur_max = max(cur_max, value)
    
    cur_max = list[-1]
    for j in range(n - 2, 0, -1):
        value = list[j]
        if value > cur_max:
            index = (i, j) if isRow else (j, i)
            cache.add(index)
            cur_max = max(cur_max, value)

def main():
    # input via .txt file
    with open('input1.txt') as f:
        lines = f.read().splitlines()
    
    grid = []
    
    for line in lines:
        grid.append([int(digit) for digit in line])
    visibleTrees = set()
    n = len(grid)
    res = n * 4 - 4

    for i in range(1, n - 1):
        getTrees(grid, i, visibleTrees, True)
        getTrees(grid, i, visibleTrees, False)
    
        
    res += len(visibleTrees)
    print(res)
    


if __name__ == "__main__":
    main()