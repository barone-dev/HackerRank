#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    aux = " " * n
    for i in range(n):
        aux = aux[1:] + "#"
        print(aux)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
