#!/bin/python3

import math
import os
import random
import re
import sys
def is_leap(year):
    leap = False
    if(year % 4 == 0 and year % 100 != 0):
        leap = True
    else:
        if(year % 400 == 0):
          leap = True
    return leap
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if (year==1918):
        return ("26.09."+str(year))
    elif 1700<=year<=1917:
        if year%4==0:
            return ("12.09."+str(year))
        else :
            return ("13.09."+str(year))
    elif 1919<=year<=2700:
        if is_leap(year)==True:
            return("12.09."+str(year))
        else:
            return("13.09."+str(year))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
