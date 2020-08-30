"""
    Hackerrank - Problem Solving
    A Very Big Sum - 03
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/compare-the-triplets/problem
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