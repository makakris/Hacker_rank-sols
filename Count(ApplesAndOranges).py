#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    q=[]
    w=[]
    for i in range(0,len(apples)):
        x=apples[i]+a
        if x>=s and x<=t:
            q.append(x)
    for j in range(0,len(oranges)):
        y=oranges[j]+b
        if y>=s and y<=t:
            w.append(y)
    print(len(q))
    print(len(w))                    


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
