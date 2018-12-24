
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    x,y=0,0
    for i in range(0,len(a)):
        if a[i]>b[i]:
            x=x+1
        elif a[i]<b[i]:
            y=y+1
        else:
            continue
    return [x,y]     
if __name__ == '__main__':

    a = list(map(int, input("enter a").rstrip().split()))

    b = list(map(int, input("enter b").rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

    
