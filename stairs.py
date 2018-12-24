import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(1,n+1):
        print((" "*(n-1))+("#"*i))
        n-=1
if __name__ == '__main__':
    n = int(input())

    staircase(n)
