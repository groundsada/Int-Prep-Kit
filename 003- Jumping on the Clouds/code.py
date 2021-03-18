#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    #we have the first and last element are always 0
    #last three elements possibilities: (110 can't be), 010, 000, 100
    #once, we reach third to last, we need one count
    #when we can stand on 4th to last: 0010, 0000,0100
    #we always need two steps
    i = 0
    count = 0
    while i < len(c)-2:
        if i == len(c)-3:
            count += 1
            break
        elif i == len(c)-4:
            count += 2
            break
        else:
            if c[i+2] == 0:
                i += 2
                count += 1
            else:
                count += 1
                i += 1
    return max(count, 1) #there is always at least one step
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
