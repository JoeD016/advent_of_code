import math
import collections

# import inbuilt standard input output
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed
def main():

    # input via .txt file
    with open('input2.txt') as f:
        lines = f.readlines()
    
    res = 0
    shape_score = {'A' : 1, 'B' : 2, 'C' : 3}
    to_win = {'A' : 'B', 'B' : 'C', 'C' : 'A'}
    to_lose = {'B' : 'A', 'C' : 'B', 'A' : 'C'}
    for line in lines:
        oponent, mine = line[0], line[2]
        if mine == 'X':
            res += shape_score[to_lose[oponent]]
        elif mine == 'Y':
            res += shape_score[oponent]
            res += 3
        else:
            res += shape_score[to_win[oponent]]
            res += 6
        
    print(res)


if __name__ == "__main__":
    main()