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
    for i in range(0, len(lines), 3):
        first = set(lines[i])
        second = set(lines[i + 1])
        third = set(lines[i + 2])
        flag = 0

        for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if char in first and char in second and char in third:
                res += ord(char) - 38
                flag = 1
                break
        
        if not flag:
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char in first and char in second and char in third:
                    res += ord(char) - 96
                    break
        
    print(res)

        


if __name__ == "__main__":
    main()