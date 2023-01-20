import math
import collections

# import inbuilt standard input output
from sys import stdin, stdout

# suppose a function called main() and
# all the operations are performed
def main():

    # input via .txt file
    with open('input1.txt') as f:
        lines = f.readlines()
    
    res = 0
    shape_score = {'X' : 1, 'Y' : 2, 'Z' : 3}
    win = {'XC', 'YA', 'ZB'}
    me_oponent = {'X':'A', 'Y':'B', 'Z':'C'}
    for line in lines:
        oponent, mine = line[0], line[2]
        res += shape_score[mine]
        if mine + oponent in win:
            res += 6
        elif me_oponent[mine] == oponent:
            res += 3
    print(res)


if __name__ == "__main__":
    main()