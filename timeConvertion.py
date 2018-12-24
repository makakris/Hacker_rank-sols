#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if 'AM' in s:
        x=s[0:2]
        if x =='12':
            x='00'
        x=x+s[2:-2]
        return x
    elif 'PM' in s:
        x=s[0:2]
        if x == '12':
            x=str(x)+s[2:-2]
        else:
            x=int(x)+12
            x=str(x)+s[2:-2]    
        return x

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
