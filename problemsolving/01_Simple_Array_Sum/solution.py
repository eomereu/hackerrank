"""
    Hackerrank - Problem Solving
    Simple Array Sum
    Difficulty: Easy
    Date: 30.08.2020
    https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import os
import sys

#
# Complete the simpleArraySum function below.
#

def simpleArraySum(ar):

    sum = 0
    for i in ar:
        sum += i
    return sum

