"""
    Hackerrank - Problem Solving
    Mini-Max Sum - 07
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/mini-max-sum/problem
"""
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    arr.sort()

    for i in range(len(arr)):
        if i >= 1:
            max_sum += arr[i]
        if i != (len(arr)-1):
            min_sum += arr[i]

    print(min_sum, max_sum)
        
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
