#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    dict = {}
    for value in ar:
        dict[value] = 0

    for i in range(0, len(ar)):
        dict[ar[i]] += 1

    print(dict)

    return dict.get(max(ar))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
