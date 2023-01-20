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

    res, temp = 0, 0
    for i in range(1, len(lines)):
        if lines[i] == '\n':
            res = max(res, temp)
            temp = 0
        else:
            temp += int(lines[i])
    print(res)
    return res



if __name__ == "__main__":
    main()