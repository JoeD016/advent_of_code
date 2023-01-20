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
    print(ord('A'), ord('a'))
    for line in lines:
        right = len(line) // 2
        cache = set(line[:right])
        for char in line[right:]:
            if char in cache:
                if ord(char) > ord('a'):
                    res += ord(char) - 96
                else:
                    res += ord(char) - 38
                break
    print(res)


if __name__ == "__main__":
    main()