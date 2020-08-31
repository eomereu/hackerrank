"""
    Hackerrank - Problem Solving
    Time Conversion - 09
    Difficulty: Easy
    Date: 31.08.2020
    https://www.hackerrank.com/challenges/time-conversion/problem
"""
import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    # s is hh:mm:ssAM OR hh:mm:ssPM
    # Assigning the hour in order to be able to increment it later as int:
    hour = int(s[:2])

    # if time is 12:mm:ssAM then turn it into 00:mm:ss
    if s[8] is "A" and hour is 12:
        return "{:02d}".format(0) + s[2:8]

    # if time is hh:mm:ssPM (but hour is not 12) then add 12 to hour 03PM +12 = 15:00
    elif s[8] is "P" and not hour is 12:
        hour += 12
        return "{}".format(hour) + s[2:8]
        
    # if time is anything else return directly
    else:
        return s[:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
