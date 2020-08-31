"""
    Hackerrank - Problem Solving
    Birthday Cake Candles - 08
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/birthday-cake-candles/problem
"""
import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(arr):
    count = 0
    max_height = max(ar)
    for i in ar:
        if i == max_height:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
