#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    lst=[[x1,v1],[x2,v2]]
    lst.sort()
    if lst[1][0]>=lst[0][0] and lst[1][1]>=lst[0][1]:
        return 'NO'
    while lst[1][0]>=lst[0][0]:
          lst[1][0]=lst[1][0]+lst[1][1]
          lst[0][0]=lst[0][0]+lst[0][1]
          if lst[1][0]==lst[0][0]:
              return 'YES'
    return 'NO'        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
