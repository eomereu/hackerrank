"""
    Hackerrank - Problem Solving
    Plus Minus - 05
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/plus-minus/problem
"""
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_positive = count_negative = count_zero = 0
    
    for i in arr:
        if i > 0:
            count_positive += 1
        elif i < 0:
            count_negative += 1
        else:
            count_zero += 1
    
    print(round(count_positive/len(arr), 6))
    print(round(count_negative/len(arr), 6))
    print(round(count_zero/len(arr), 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
