"""
    Hackerrank - Problem Solving
    Apple and Orange - 11
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/apple-and-orange/problem
"""
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_locations = []
    oranges_locations = []
    apples_count = oranges_count = 0
    
    for i in apples:
        apples_locations.append(a + i)
    
    for i in oranges:
        oranges_locations.append(b + i)
    
    for i in apples_locations:
        if i >= s and i <= t:
            apples_count += 1 
    
    for i in oranges_locations:
        if i >= s and i <= t:
            oranges_count += 1
    
    print(apples_count)
    print(oranges_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
