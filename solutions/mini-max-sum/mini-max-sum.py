#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    quickSort(arr, 0, len(arr) - 1)
    print(sum_range(arr[0:4]), sum_range(arr[1:5]))


def sum_range(arr):
    sum = 0
    for value in arr:
        sum += value

    return sum


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
