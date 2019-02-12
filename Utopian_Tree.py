#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height=[1]
    num=2
    for i in range(0,n):
        if num%2==0:
            height+=[num]
            num=num+1
        else:
            height+=[num]
            num=num*2
    return max(height)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
