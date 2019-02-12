#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def rev(x):
    c=0
    while x>0:
        a=x%10
        b=a+c
        c=b*10
        x=x//10
    return b

def beautifulDays(i, j, k):
    count=0
    for m in range(i,j+1):
        a=abs(m-rev(m))/k
        if a == int(a):
            count=count+1
    return count        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
