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

    res, temp = [0, 0, 0], 0
    for i in range(1, len(lines)):
        if lines[i] == '\n':
            low = min(res)
            if temp > low:
                res[res.index(low)] = temp
            temp = 0
        else:
            temp += int(lines[i])
    print(sum(res))
    # return res



if __name__ == "__main__":
    main()