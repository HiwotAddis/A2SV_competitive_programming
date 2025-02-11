# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    max_=99
    count=[0]*(max_+1)
    for num in arr:
        count[num]+=1
    target = 0
    for index, val in enumerate(count):
        for i in range(val):
            arr[target] = index
            target += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
