#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repeats,remains,count = n // len(s), n % len(s), 0
    for i in range(remains):
        if s[i] == "a":
            count += repeats +1
    for i in range(remains,len(s)):
        if s[i] == "a":
            count += repeats
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
