# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    i=n-2
    key=arr[n-1]
    while i>=0 and arr[i]>key:
        arr[i+1]=arr[i]
        print(*arr)
        i-=1
    arr[i+1]=key
    print(*arr) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
