#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    i = 0
    for j in range(1, len(arr)):
        if j-i > 1:
            if arr[j] < p:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        else:
            if arr[j] < p:
                i += 1
    arr[0], arr[i] = arr[i], arr[0]
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
