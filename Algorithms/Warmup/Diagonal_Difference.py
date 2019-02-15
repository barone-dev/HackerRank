#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    n = len(arr[0])
    a_point = 0
    b_point = n-1
    dig_a = 0
    dig_b = 0
    for line in arr:
        dig_a += line[a_point]
        dig_b += line[b_point]
        a_point += 1
        b_point -= 1
    return abs(dig_a - dig_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
