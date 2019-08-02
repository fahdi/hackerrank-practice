#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    results = [0, 0]
    for i in range(0, len(a)):
        if a[i] < b[i]:
            results[1] += 1
        if a[i] > b[i]:
            results[0] += 1

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
