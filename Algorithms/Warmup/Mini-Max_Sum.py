#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sum, arr_min, arr_max = sum(arr), min(arr), max(arr)
    print(f"{arr_sum-arr_max} {arr_sum-arr_min}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
