"""
    Hackerrank - Problem Solving
    Compare The Triplets - 02
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scores_alice_bob = [0, 0]
    i = 0

    while i < 3:
        if a[i] > b[i]:
            scores_alice_bob[0] += 1
        elif a[i] < b[i]:
            scores_alice_bob[1] += 1
        i += 1
                
    return scores_alice_bob