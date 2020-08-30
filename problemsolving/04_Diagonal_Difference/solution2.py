"""
    Hackerrank - Problem Solving
    Diagonal Difference - 04
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    left_to_right_diagonal_sum = 0
    right_to_left_diagonal_sum = 0

    # Appending the items arr[0][0] arr[1][1] arr[2][2] and so on
    #  to the left_to_right_diagonal array
    for i in range(len(arr)):
        left_to_right_diagonal_sum += arr[i][i]
    
    # Appending the items arr[0][3] arr[1][2] arr[2][1] and so on
    #  to the right_to_left_diagonal array
    for i in range(len(arr)):
        right_to_left_diagonal_sum += arr[i][len(arr)-1-i]

    return abs(left_to_right_diagonal_sum-right_to_left_diagonal_sum)

# Main function
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
