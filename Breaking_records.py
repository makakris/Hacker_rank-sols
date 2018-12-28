#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest=scores[0]
    lowest=scores[0]
    count_x=0
    count_y=0
    for i in range(1,len(scores)):
        if int(scores[i]) > highest:
            highest=scores[i]
            count_x+=1
        elif int(scores[i])<lowest:
            lowest=scores[i]
            count_y+=1
    return [count_x,count_y]       
    


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
