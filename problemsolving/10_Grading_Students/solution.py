"""
    Hackerrank - Problem Solving
    Grading Students - 10
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/grading/problem
"""
import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] > 37:
            if grades[i] % 5 is 3:
                grades[i] += 2
            elif grades[i] % 5 is 4:
                grades[i] += 1
    return grades

# 
# 60 % 5 = 0
# 61 % 5 = 1
# 62 % 5 = 2 | 65 - 62 = 3 ... NOT < 3 NO
# 63 % 5 = 3 | 65 - 63 = 2 ... < 3 OK
# 64 % 5 = 4 | 65 - 64 = 1 ... < 3 OK
# 65 % 5 = 0
# 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
