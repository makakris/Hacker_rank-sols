#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_a=0
    count_b=0
    for i in range(0,len(apples)):
        apples[i]=apples[i]+a
    for j in range(0,len(oranges)):
        oranges[j]=oranges[j]+b
    for x in range(0,len(apples)):
        if apples[x]>=s and apples[x]<=t:
            count_a=count_a+1
    for y in range(0,len(oranges)):
        if oranges[y]>=s and oranges[y]<=t:
            count_b=count_b+1
    print(count_a)
    print(count_b)                    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
