"""
    Hackerrank - Problem Solving
    A Very Big Sum - 03
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/a-very-big-sum/problem
"""
import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

# Main function
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
