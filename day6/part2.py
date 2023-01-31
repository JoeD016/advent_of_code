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

    input = lines[0]
    left, right = 0, 13
    cache = collections.defaultdict(int)
    for i in range(left, 14):
        cache[input[i]] += 1
    
    while right < len(input) - 1:
        if len(cache) == 14:
            print(right + 1)
            return 
        cache[input[left]] -= 1
        if cache[input[left]] == 0:
            del cache[input[left]]
        right += 1
        cache[input[right]] += 1
        left += 1
    return 

        



if __name__ == "__main__":
    main()