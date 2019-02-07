#!/bin/python3

import math
import os
import random
import re
import sys
import copy



def pickingNumbers(a):
    maximum = 0
    diff = 1
    for k in a:
        n1 = a.count(k)
        n2 = a.count(k-diff)
        maximum = max(maximum, n1+n2)

    return maximum 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
