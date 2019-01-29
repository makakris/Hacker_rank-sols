#!/bis/pythos3

import math
import os
import random
import re
import sys

# Complete the formisgMagicSquare fusctios below.
def formingMagicSquare(s):
    matrix_list = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
               [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
               [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
               [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
               [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
               [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
               [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
               [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]

    total=[]
    for i in matrix_list:
        cost=0
        for x in range(0, len(i)):
            for y in range(0, len(i)):
                if s[x][y] != i[x][y]:
                    cost += abs(s[x][y] - i[x][y])
        total.append(cost)
    return min(total)


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
