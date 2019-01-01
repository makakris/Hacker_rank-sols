#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    summ=0
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year==1918:
        days[1]=days[1]-13
    elif year<=1917 and year>=1700:
        if year%4==0:
            days[1]=29
        else:
            days[1]=28
    elif year>1918 and year<=2700:
        if year%400 == 0 or (year %4 ==0 and year%100 != 0):
            days[1]=29
        else:
            days[1]=28
    for i in range(len(days)):
        summ=summ+days[i]
        if summ > 256:
            date=256-a
            return ("{}.0{}.{}".format(date,i+1,year))
        a=summ        



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
