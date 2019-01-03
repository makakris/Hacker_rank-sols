#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p <= n/2:
        return (p)//2
    elif n%2==0:
        return math.ceil((n-p)/2)
    else:
        return (n-p)//2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
