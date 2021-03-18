#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar = sorted(ar)
    current = ar[0]
    count = 0
    for i in ar:
        if i == current:
            count += 1
        else:
            count = count // 2 * 2
            current = i
            count += 1
    return count // 2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
