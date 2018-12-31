#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    i=0
    x=[]
    y=[]
    b=list(set(arr))
    while i<len(arr):
        x.append(arr.count(arr[i]))
        i = i+ arr.count(arr[i])
    for i in range(len(x)):
            if x[i]==max(x):
                y.append([x[i],b[i]])
    y.sort()
    return y[0][1]        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
