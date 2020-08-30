"""
    Hackerrank - Problem Solving
    Simple Array Sum - 01
    Difficulty: Easy
    Date: 30.08.2020
    https://www.hackerrank.com/challenges/simple-array-sum/problem
"""
import os
import sys

# Complete the simpleArraySum function below.
def simpleArraySum(ar):

    sum = 0
    for i in ar:
        sum += i
    return sum

# Main function
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    