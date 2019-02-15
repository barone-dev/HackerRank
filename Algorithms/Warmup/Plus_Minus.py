#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p, n, z = 0, 0, 0
    for i in arr:
        if i == 0:
            z += 1
        elif i > 0:
            p += 1
        else:
            n += 1
    return p, n, z

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    pnz = plusMinus(arr)
    for i in pnz:
        print(f'{i/n:.6f}')
